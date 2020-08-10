# bot.py
import os
import random
from datetime import datetime
from pytz import timezone
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.command(name='buzz')
async def buzz(ctx):

    current = datetime.now(tz=timezone('America/Phoenix'))
    current = current.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    # response = f'buzzed at {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")}'

    await ctx.send("{} buzzed at {}".format(ctx.message.author.mention, current))

bot.run(TOKEN)
