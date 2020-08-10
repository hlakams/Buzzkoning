import os
import random
from datetime import datetime
from pytz import timezone
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # calls from '.env'

bot = commands.Bot(command_prefix='/') # action on '/*'

@bot.command(name='buzz') # bot calls on '/buzz' and formats to specified timezone
async def buzz(ctx):

    current = datetime.now(tz=timezone('America/Phoenix')) # specify timezone
    current = current.strftime("%d-%b-%Y (%H:%M:%S.%f)") # set datetime string format

    await ctx.send("{} buzzed at {}".format(ctx.message.author.mention, current)) # print buzz

bot.run(TOKEN) # run bot
