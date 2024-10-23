import asyncio
import os

import uvloop
from arq.connections import RedisSettings
from app.core.config import settings

# 設定使用 uvloop 作為事件循環策略
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# NOTE(Marcelo): 我們是否希望在工作者和應用程序中使用相同的環境變數？
REDIS_HOST = settings.REDIS_HOST  # 獲取 Redis 主機，默認為 localhost
REDIS_PORT = settings.REDIS_PORT      # 獲取 Redis 端口，默認為 6379

# 定義一個異步任務，接受上下文和字串作為參數
async def test_task(ctx, word: str):
    await asyncio.sleep(10)  # 模擬一個耗時的操作，暫停 10 秒
    return f"test task return {word}"  # 返回結果

# 當工作者啟動時執行的異步函數
async def startup(ctx):
    print("start")  # 輸出啟動訊息

# 當工作者關閉時執行的異步函數
async def shutdown(ctx):
    print("end")  # 輸出結束訊息

# WorkerSettings 類，用於配置工作者的設置
class WorkerSettings:
    functions = [test_task]  # 設定可用的任務函數列表
    redis_settings = RedisSettings(host=REDIS_HOST, port=REDIS_PORT)  # 配置 Redis 設置
    on_startup = startup  # 設定啟動時要執行的函數
    on_shutdown = shutdown  # 設定關閉時要執行的函數
    handle_signals = False  # 是否處理系統信號（如中斷信號）