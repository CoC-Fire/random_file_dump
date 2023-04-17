import time

import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    intents = intents,
    command_prefix = '>'
)

async def spammer():
    symbol = '﷽'
    channel_id = 1234567890
    await bot.get_channel(channel_id).send(symbol * 2000)
    time.sleep(0.8)

@bot.event
async def on_ready():
    while True:
        await spammer()

bot.run('bot_token')
