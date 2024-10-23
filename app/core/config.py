from typing import Any, Dict, Optional
from pydantic_settings import BaseSettings
from pydantic import EmailStr, SecretStr, field_validator

# 定義 Settings 類，繼承自 BaseSettings，用於管理應用程序的配置
class Settings(BaseSettings):
    PROJECT_NAME: str ="PROJECT_NAME" # 項目名稱

    POSTGRES_DB: str  # PostgreSQL 數據庫名稱
    POSTGRES_HOST: str  # PostgreSQL 主機地址
    POSTGRES_USER: str  # PostgreSQL 用戶名
    POSTGRES_PASSWORD: SecretStr  # PostgreSQL 密碼，使用 SecretStr 以保護敏感信息
    # TODO(Marcelo): 在合併 https://github.com/samuelcolvin/pydantic/pull/2567 後更改類型
    POSTGRES_URI: Optional[str] = None  # 可選的 PostgreSQL URI

    # 驗證器：用於生成 PostgreSQL 連接 URI
    @field_validator('POSTGRES_URI')
    def validate_postgres_conn(cls, v: Optional[str], info) -> str:
        if isinstance(v, str):
            return v  # 如果已提供 URI，則直接返回
        
        # 獲取其他字段的值
        values = info.data  # 獲取整個模型的數據
        password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr(""))
        
        # 格式化並返回 PostgreSQL URI
        return "{scheme}://{user}:{password}@{host}/{db}".format(
            scheme="postgresql+asyncpg",  # 使用 asyncpg 驅動
            user=values.get("POSTGRES_USER"),
            password=password.get_secret_value(),  # 獲取密碼的明文值
            host=values.get("POSTGRES_HOST"),
            db=values.get("POSTGRES_DB")
        )

    FIRST_USER_EMAIL: EmailStr  # 首位用戶的電子郵件地址
    FIRST_USER_PASSWORD: SecretStr  # 首位用戶的密碼

    SECRET_KEY: SecretStr  # 應用程序的秘密金鑰，用於加密等操作
    ACCESS_TOKEN_EXPIRE_MINUTES: int  # 訪問令牌過期時間（分鐘）

    REDIS_HOST: str  # Redis 主機地址
    REDIS_PORT: int  # Redis 端口號

    class Config:
        env_file = ".env"  # 指定 .env 檔案

# 創建 Settings 實例，將配置加載到 settings 對象中
# 創建 Settings 實例以測試
settings = Settings()

print(settings.POSTGRES_URI)  # 應該會輸出正確的 URI