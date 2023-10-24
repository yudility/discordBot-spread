import discord
from discord.ext import commands
from spreadtest import *

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

file = open("keys/key.txt",'r')
key = file.read()
file.close()

@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=None)
    
    
@bot.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')


@bot.command()
async def talk(ctx, arg1, arg2):
    await ctx.reply('{} talks to {}.'.format(arg1, arg2))

@bot.command()
async def addMe(ctx, arg1, arg2):
    await ctx.reply('{} add {}.'.format(arg1, arg2))

myRole = 'myRole'

@bot.command()
@commands.has_any_role(myRole)
async def cool(ctx):
    await ctx.send('You are cool indeed {}.'.format(myRole))
    
@bot.command()
async def addPersonTest(ctx, arg1, arg2, arg3):
    addPerson(arg1, arg2, arg3)
    await ctx.send('참여 완료! 가문명: {} , 직업: {} , 전/각: {} '.format(arg1,arg2,arg3))

bot.run(key)

