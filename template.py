import discord
from discord.ext import commands
import requests

permissão = discord.Intents.default()
permissão.message_content = True
robo = commands.Bot(command_prefix="!", intents=permissão)

@robo.command()
async def olá(ctx):
    await ctx.send("Olá, meu nome é GrowTrees.IA! Como posso te ajudar?")

 
robo.run("token")
