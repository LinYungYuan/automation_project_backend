
from arq import create_pool
from arq.connections import RedisSettings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.core import redis
from app.core.config import settings
from app.core.logger import get_logger, log_middleware


logger = get_logger(__name__)

# 異步函數：創建 Redis 連接池
async def create_redis_pool():
    # 使用 create_pool 函數創建連接池，並將其分配給 redis 模塊中的 pool 屬性
    redis.pool = await create_pool(
        RedisSettings(host=settings.REDIS_HOST, port=settings.REDIS_PORT)  # 使用項目設置中的 Redis 主機和端口
    )

# 異步函數：關閉 Redis 連接池
async def close_redis_pool():
    # 調用 close 方法關閉連接池
    await redis.pool.close()

# 創建 FastAPI 應用程序的函數
def create_application() -> FastAPI:
    # 初始化 FastAPI 應用程序並設置項目名稱
    application = FastAPI(title=settings.PROJECT_NAME)
    
    # 將路由器添加到應用程序中，以處理 API 請求
    application.include_router(router)
    
    # 在應用程序啟動時調用 create_redis_pool 函數以建立 Redis 連接池
    application.add_event_handler("startup", create_redis_pool)
    
    # 在應用程序關閉時調用 close_redis_pool 函數以關閉 Redis 連接池
    application.add_event_handler("shutdown", close_redis_pool)
    # 添加中間件以記錄請求和響應信息
    application.middleware("http")(log_middleware)
    # 添加 CORS 中間件以允許跨域請求
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Angular開發伺服器的URL
        allow_credentials=True,  # 允許攜帶憑證
        allow_methods=["*"],  # 允許所有HTTP方法
        allow_headers=["*"],  # 允許所有headers
        
    )
    # 返回創建的 FastAPI 應用程序實例
    return application

# 創建 FastAPI 應用程序實例並賦值給 app 變量
app = create_application() 
