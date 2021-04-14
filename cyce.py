
import discord
from discord.ext import commands
token = "ODI3MTg2ODAyMzU5NTMzNjM4.YGXXvg.LatAKANS8zoU4FQb0TJ_ej5C83o"
client = commands.Bot(command_prefix= "*")

@client.event
async def on_message(message):
    if message.content == 'siema':
        await message.channel.send('cześć')
        await message.channel.send('@', message.author)


client.run(token)
