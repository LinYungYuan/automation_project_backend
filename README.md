# automation_project_backend
第一次使用python fastapi 和 sqlalchemy 當作練習來開發後端服務 \
db使用postgresql，搭配BaseModel來定義資料的檢核及序列化 \
接下來嘗試串接redis來優化儲存user session 
### 資料夾結構
models資料夾定義資料表的欄位 \
crud資料夾定義資料表的增刪改查 \
schemas資料夾定義資料的檢核及序列化 \
core資料夾定義資料庫的連線, redis的連線, security驗證密碼取jwt token \
deps.py定義jwt的驗證 \
health.py定義health check的路徑 \
待續...

# table設定
![db關聯](./db.png)

### User 使用者資料表
user_id, name, email, password, is_active, is_superuser 

-- 建立User資料表（使用AUTO_INCREMENT）\
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    password VARCHAR(255),
    is_active BOOLEAN,
    is_superuser BOOLEAN
);

### Chat 聊天資料表
chat_id, user_id, title, created_at, updated_at

-- 建立Chat資料表（使用AUTO_INCREMENT）\
CREATE TABLE Chat (
    chat_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title NVARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

### Message 訊息資料表
message_id, chat_id, content, is_bot, created_at, updated_at

-- 建立Message資料表 \
CREATE TABLE Message (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id INT,
    content TEXT,
    is_bot BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES Chat(chat_id)
);

# 服務啟動指令
pip install -r requirements.txt \
uvicorn app.main:app --reload





