# automation_project_backend

使用python fastapi 和sqlalchemy 來開發後端服務
db使用postgresql

## table設定
User 使用者資料表
user_id, name, email, password, is_active, is_superuser

-- 建立User資料表（使用AUTO_INCREMENT）
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    password VARCHAR(255),
    is_active BOOLEAN,
    is_superuser BOOLEAN
);

Chat 聊天資料表
chat_id, user_id, title, created_at, updated_at

-- 建立Chat資料表（使用AUTO_INCREMENT）
CREATE TABLE Chat (
    chat_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title NVARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

Message 訊息資料表
message_id, chat_id, content, is_bot, created_at, updated_at

-- 建立Message資料表
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
pip install -r requirements.txt
uvicorn app.main:app --reload





