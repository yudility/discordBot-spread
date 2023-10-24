import discord
from discord.ext import commands
import spreadtest

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

bot.run(key)

