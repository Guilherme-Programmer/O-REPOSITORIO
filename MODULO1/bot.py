import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou Jarvis!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Até mais!')

@bot.command()
async def helpcommands(ctx):
    await ctx.send(f'Comandos utilizáveis: $hello, $bye, $heh, $helpcommands, $joke1, $joke2, $joke3, $joke4)')

@bot.command()
async def joke1(ctx):
    await ctx.send(f'Como se chama um cadeirante pegando fogo? Um HotWheels!')

@bot.command()
async def joke2(ctx):
    await ctx.send(f'O que é um pontinho vermelho no meio da mata? Um Morangotango!')

@bot.command()
async def joke3(ctx):
    await ctx.send(f'O que é um pontinho vermelho em um castelo? A Pimenta Do Reino!')

@bot.command()
async def joke4(ctx):
    await ctx.send(f'O que é um pontinho amarelo no meio do oceano? O Ruffles, a Batata da Onda!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("He" + "he" * count_heh)

bot.run("Token")
