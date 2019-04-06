import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
  await bot.change_presence(game=discord.Game(name='auf RageGames [/help]'))
  
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
  await bot.ban(target)
  await bot.say('Der User wurde erfolgreich gebannt!')
  
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member)
  await bot.kick(target)
  await bot.say('Der User wurde erfolgreich gekickt!')
  
bot.run('NTYzMTE0NjI1NTAwMDUzNTA1.XKi-RQ.C_Eph_IIvWV8IP8V7y_MFJZZkdw')
