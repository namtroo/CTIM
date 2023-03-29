#!/usr/bin/env python3

import telegram
import subprocess
import asyncio

class Notifier:
    def __init__(self, token, chat_id):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id
    
    async def send_notification(self):
        # Send a message by taking output of config.py
        message = subprocess.check_output(['python', 'config.py'])
        message_str = message.decode()
        await self.bot.send_message(chat_id=self.chat_id, text=message_str)
    
if __name__ == "__main__":
    # Set up the bot and chat_id
    # My group use to test
    bot_token = '5778730071:AAHU3Ti-FCSnY4KqcIsqYrIUrgitMOb0kVw'
    chat_id = '-1001714864670'
    telegram_bot = Notifier(token=bot_token, chat_id=chat_id)
    asyncio.run(telegram_bot.send_notification())
