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


global countOne # var for room #1 counter

@bot.command(name='one') # question count for room #1
async def one(ctx):

    global countOne
    countOne += 1
    await ctx.send("Room 1\n----------\nQuestion {}\n----------\n".format(countOne))


@bot.command(name='oneC') # reinitialize countOne
async def oneC(ctx):

    global countOne
    countOne = 0
    await ctx.send("*Round for Room #1 has been Reset*")


global countTwo # var for room #2 counter

@bot.command(name='two') # question count for room #2
async def two(ctx):

    global countTwo
    countTwo += 1
    await ctx.send("Room 2\n----------\nQuestion {}\n----------\n".format(countTwo))


@bot.command(name='twoC') # reinitialize countTwo
async def twoC(ctx):

    global countTwo
    countTwo = 0
    await ctx.send("*Round for Room #2 has been Reset*")


bot.run(TOKEN) # run bot
