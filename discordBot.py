import discord
from discord.ext import commands
from spreadtest import *

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

file = open("keys/key.txt",'r')
key = file.read()
file.close()

dot_role = '돚거단'
inst_role = '파본'

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

@bot.command()
@commands.has_any_role(dot_role)
async def cool(ctx):
    await ctx.send('You are hot indeed {}.'.format(dot_role))

     
# @bot.command()
# async def addPersonTest(ctx, arg1, arg2, arg3):
#     addPersonToDot(arg1, arg2, arg3)
#     await ctx.send('참여 완료! 가문명: {} , 직업: {} , 전/각: {} '.format(arg1,arg2,arg3))

# @bot.command()
# async def at(ctx, 요일, 닉네임, 직업, 전각):
#     addtest(요일,닉네임, 직업, 전각)
#     await ctx.send('참여 완료! 가문명: {} , 직업: {} , 전/각: {} '.format(요일,닉네임,직업,전각))

@bot.command()
async def 참여신청(ctx, 닉네임, 직업, 전각):
    
    addPersonToDot(닉네임, 직업, 전각)
    await ctx.send('참여 완료! 가문명: {} , 직업: {} , 전/각: {} '.format(닉네임,직업,전각))


@bot.command()
async def 참여인원확인(ctx, 요일):
    await ctx.send('{} 거점 인원은 ', getNumberWeek(요일), '입니다.')



@bot.command()
async def 거점일정확인(ctx):
    date_info = getDate()

    values_as_strings = [str(value) for value in date_info.values()]

    all_date = ' / '.join(values_as_strings)

    await ctx.send('<이번주 거점 일정>\n :'+ all_date)
    await ctx.send('참여 신청 명령어 - /참여신청 닉네임 직업 전각')

bot.run(key)

