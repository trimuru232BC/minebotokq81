from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests, urllib3
from urllib.parse import urlparse
import os
import time
from PIL import ImageGrab
from pyautogui import screenshot
ADMIN_USER_ID = 5244246071
TOKEN: Final = '6856047619:AAGLmBE-4eMv-YaWUSsAJxTMvvXBw8XOKM0'
urllib3.disable_warnings()
def is_server_running():
    processes = os.popen("tasklist").read()
    return "BEDROC~1.EXE" in processes
async def sss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        image = screenshot()
        image.save("screenshot.png")
        await update.message.reply_photo(open("screenshot.png", "rb"))
async def start_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        if is_server_running():
            await update.message.reply_text("Server đã chạy trước đó! ❌")
            return
        file_path = "bin/startsv.gif"
        try:
            with open(file_path, "rb") as f:
                await context.bot.send_document(update.message.chat_id, f)
        except FileNotFoundError as e:
            print("error not found")
        except Exception as e:
            print(f"error {e}")
        time.sleep(2)
        await update.message.reply_text("Server đang khởi động...")
        file_path = r"C:\Users\Administrator\Desktop\bedrock-server-1.20.62.03\bedrock_server.exe"
        os.startfile(file_path)
        time.sleep(2)
        await update.message.reply_text("Server khởi động thành công ✅")
        image = screenshot()
        image.save("screenshot.png")
        await update.message.reply_photo(open("screenshot.png", "rb"))
async def stop_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        file_path = "bin/stop.gif"
        try:
            with open(file_path, "rb") as f:
                await context.bot.send_document(update.message.chat_id, f)
        except FileNotFoundError as e:
            print("error not found")
        except Exception as e:
            print(f"error {e}")
        time.sleep(3)
        if not is_server_running():
            await update.message.reply_text("Server đã tắt trước đó! ❌")
            return
        await update.message.reply_text("Server đang tắt...")
        os.system("taskkill /F /IM BEDROC~1.EXE")
        await update.message.reply_text("Đóng server thành công ✅")
        image = screenshot()
        image.save("screenshot.png")
        await update.message.reply_photo(open("screenshot.png", "rb"))
async def restart_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        if not is_server_running():
            await update.message.reply_text("Server đã tắt trước đó! ❌")
            return
        else:
            file_path = "bin/restart.gif"
        try:
            with open(file_path, "rb") as f:
                await context.bot.send_document(update.message.chat_id, f)
        except FileNotFoundError as e:
            print("error not found")
        except Exception as e:
            print(f"error {e}")
        time.sleep(5)
        await update.message.reply_text("Đang khởi động lại server...")
        os.system("taskkill /F /IM BEDROC~1.EXE")
        file_path = r"C:\Users\Administrator\Desktop\bedrock-server-1.20.62.03\bedrock_server.exe"
        os.startfile(file_path)
        time.sleep(2)
        await update.message.reply_text("Server khởi động lại thành công ✅")
        image = screenshot()
        image.save("screenshot.png")
        await update.message.reply_photo(open("screenshot.png", "rb"))
async def startcm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        file_path = "bin/start.gif"
        try:
            with open(file_path, "rb") as f:
                await context.bot.send_document(update.message.chat_id, f)
        except FileNotFoundError as e:
            print("error not found")
        except Exception as e:
            print("error")
        time.sleep(1)
        await update.message.reply_text(
f'''Hello user
━━━━━━━━━━━━━━
TOOL KIỂM TRA SERVER MINECRAFT ✅
━━━━━━━━━━━━━━
Nhập /cmds hoặc /help để hiển thị lệnh ✅
━━━━━━━━━━━━━━
Bot tạo bởi Tuấnn''')
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        file_path = "bin/help.gif"
        try:
            with open(file_path, "rb") as f:
                await context.bot.send_document(update.message.chat_id, f)
        except FileNotFoundError as e:
            print("error not found")
        except Exception as e:
            print(f"error {e}")
        await update.message.reply_text(
f'''Danh sách lệnh
━━━━━━━━━━━━━━
- /chksv: Kiểm tra server
- /startsv: Chạy server
- /stop: Dừng server
- /restart: Khởi động lại server
- /checkss: Check màn hình
━━━━━━━━━━━━━━
Bot tạo bởi Tuấnn''')
async def chksv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You không phải admin! ❌")
    else:
        try:
            file_path = "bin/chksv.gif"
            try:
                with open(file_path, "rb") as f:
                    await context.bot.send_document(update.message.chat_id, f)
            except FileNotFoundError as e:
                print("error not found")
            except Exception as e:
                print("error")
            time.sleep(5)
            response = requests.get("https://api.mcstatus.io/v2/status/bedrock/often-photographer.gl.at.ply.gg:11256")
            data = response.json()
            if data["online"]:
                host = data["host"]
                port = data["port"]
                version = data["version"]
                players = data["players"]
                motd = data["motd"]
                gamemode = data["gamemode"]
                server_id = data["server_id"]
                edition = data["edition"]
                await update.message.reply_text(
f'''Hello admin Tuấnn!
━━━━━━━━━━━━━━
TRÌNH KIỂM TRA SERVER MINECRAFT ✅
━━━━━━━━━━━━━━
* Trạng thái: Hoạt động ✅
* Server: {host}
* Port: {port}
* Phiên bản: {version['name']} (Protocol: {version['protocol']})
* Người chơi: {players['online']} / {players['max']}
* MotD: 
{motd['clean']}
* Gamemode: {gamemode}
* Server ID: {server_id}
* Edition: {edition}
━━━━━━━━━━━━━━
Bot tạo bởi Tuấnn''')
            else:
                host = data["host"]
                port = data["port"]
                await update.message.reply_text(
f'''Hello admin Tuấnn!
━━━━━━━━━━━━━━
TRÌNH KIỂM TRA SERVER MINECRAFT ✅
━━━━━━━━━━━━━━
* Trạng thái: Đóng ❌
* Server: {host}
* Port: {port}
━━━━━━━━━━━━━━
Bot tạo bởi Tuấnn''')
        except:
            await update.message.reply_text(f"Lỗi mất quyền kiểm soát❌")
if __name__=='__main__':
    print('Wibu is on top 10%....')
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', startcm))
    app.add_handler(CommandHandler('cmds', help))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('chksv', chksv))
    app.add_handler(CommandHandler('startsv', start_server))
    app.add_handler(CommandHandler('stop', stop_server))
    app.add_handler(CommandHandler('restart', restart_server))
    app.add_handler(CommandHandler('checkss', sss))
    print('.....100%')
    app.run_polling(poll_interval=3)
