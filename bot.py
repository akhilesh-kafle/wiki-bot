import os
import discord
from dotenv import load_dotenv
import wikipedia

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'{client.user} is in discord')


@client.event
async def on_message(message):
    user_name = str(message.author)
    user_message = str(message.content)
    print(user_name)
    print(user_message)
    channel_name = str(message.channel.name)
    print(channel_name)
    if message.author == client.user:
        return
    else:
        if user_message.lower()[0] == "!":
            print(user_message.lower()[0])
            summary = wikipedia.summary(user_message.lower()[1:],sentences="3")
            print(summary)
            await message.channel.send(summary)

client.run(TOKEN)