from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Başarıyla", self.user, "olarak giriş yapıldı.")

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None, None
    
        for text in ['/ai','/uyanbot','/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')  
                print(command, user_message)

        if command  == '/ai' or command == '/uyanbot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Cevap: {bot_response}")       

intents = discord.Intents.default()
intents.message_content = True 
client = MyClient(intents=intents)  