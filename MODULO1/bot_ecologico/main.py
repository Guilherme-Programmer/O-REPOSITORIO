import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content= True

bot = commands.Bot(command_prefix="!!", intents=intents)

lixos_certos = {
    "Azul": "Papelão ou Papel",
    "Vermelho": "Plástico ou Isopor",
    "Verde": "Vidro",
    "Amarelo": "Metal",
    "Preto": "Madeira",
    "Laranja": "Item perigoso ou contaminados",
    "Branco": "Ambulatórios ou de serviço de saúde",
    "Roxo": "Radioativos",
    "Marrom": "Orgânicos",
    "Cinza": "Não recicláveis ou misturados"
}
lembrar = {
    "Não se esqueça de mim quando ver um lixo!",
    "Não esqueça das minhas informações envolvendo lixo!",
    
}
@bot.event
async def on_ready():
    print(f"Estamos logados como {bot.user}")
    print("O bot está pronto para te ajudar!")
    
@bot.command
async def help(ctx):
    await ctx.send(f"Olá, como posso te ajudar? Escolha uma dessas opções:!!lixoscorretos e a cor que quer saber sobre")
    
@bot.command
async def lixoscorretos(ctx, lixo, str):
    lixo = lixo.lower()
    if lixo in lixos_certos:
        await ctx.send(f"{lixo.capitalize()}:  {lembrar[lixos_certos]}")
    



bot.run("TOKEN")