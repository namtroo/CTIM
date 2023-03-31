#!/usr/bin/env python3

import telegram
import subprocess
import asyncio
from config import token, chat_id

class Notifier:
    def __init__(self, token, chat_id):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id
    
    async def send_notification(self):
        # Send a message by taking output of config.py
        message = subprocess.check_output(['python', 'config.py'])
        message_str = message.decode()
        await self.bot.send_message(chat_id=self.chat_id, text=message_str)

    def set_bot(self, bot_token, chat_id):    
        # Set up the bot and chat_id
        self.token = bot_token
        self.chat_id = chat_id
        telegram_bot = Notifier(token=self.token, chat_id=self.chat_id)
        asyncio.run(telegram_bot.send_notification())
