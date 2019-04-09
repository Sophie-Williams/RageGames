import discord
from discord.ext import commands
import asyncio
import random
from discord import game

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
  await bot.change_presence(game=discord.Game(name='auf RageGames [/help]'))
  
@bot.event
async def on_message(message):
  if message.content.startswith('/allesodernichts')
  randomlist = ['Du kriegst 100000$','Du bekommst garnichts HAHAHA',]
  await bot.send_message(message.channel,(random.choice(randomlist)))
  
@bot.event
async def on_member_join(member):
  print('Ich habe erfahren dass der User' + member.name + 'gejoint ist!')
  await bot.send_message(member, 'Vielen Dank, dass du dem Server RageGames gejoint bist. wir haoffen du hast noch viel Spaß._.')
  print('Send message to ' + member.name)
  
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
  await bot.ban(target)
  await bot.say('Der User wurde erfolgreich gebannt!')
  
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member)
  await bot.kick(target)
  await bot.say('Der User wurde erfolgreich gekickt!')
  
bot.run('BOT_TOKEN')
