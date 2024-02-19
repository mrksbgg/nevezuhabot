import sqlite3
import os

from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler
from config import (
    token as bot_token,
    api_id,
    api_hash,
    version,
    adminid
)

app = Client(
    "nevezuhabot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# этот бот был сделан за минут 5, простите за говнокод
@app.on_message()
def nevezuha(client, message):
    app.send_video(message.chat.id, "nevezuha.mp4")

if __name__ == '__main__':
    my_handler = MessageHandler(nevezuha)
    app.add_handler(my_handler)
    try:
        app.start()
        me = app.get_me()
    except sqlite3.OperationalError as e:
        print(f"[Error] Ошибка: Сессия занята другим процессом! ({e})")
        os.remove("nevezuhabot.session")
        print("f[Info] Рестарт...")
        app.start()
        me = app.get_me()
    print(f"[Info] Бот был запущен и авторизован как {me.first_name} (@{me.username})")
    app.send_message(adminid, f"Бот запущен! Версия: v{version}")
    idle()
