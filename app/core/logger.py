import logging
import sys
from pathlib import Path
from loguru import logger
from fastapi import Request

# 設定日誌檔案路徑
LOG_PATH = Path("logs")
LOG_PATH.mkdir(parents=True, exist_ok=True)
# 設定日誌級別
logging.basicConfig(level=logging.INFO)

# 日誌格式
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

# 配置日誌
logger.configure(
    handlers=[
        # 控制台輸出
        {"sink": sys.stdout, "format": log_format, "level": "INFO"},
        # 檔案輸出
        {"sink": LOG_PATH / "app.log", "format": log_format, "rotation": "500 MB", "level": "INFO"},
        # 錯誤日誌
        {"sink": LOG_PATH / "error.log", "format": log_format, "rotation": "500 MB", "level": "ERROR"},
    ]
)

# 異步日誌中間件
async def log_middleware(request: Request, call_next):
    # 請求前記錄
    logger.info(f"Request: {request.method} {request.url}")
    logger.info(f"Headers: {request.headers}")
    
    # 處理請求
    response = await call_next(request)
    
    # 請求後記錄
    logger.info(f"Response Status: {response.status_code}")
    
    return response

# 取得logger實例
def get_logger(name: str):
    return logger.bind(name=name)