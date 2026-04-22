import discord
from discord.ext import commands
import os
import random
import requests

''' w — grava dados em um arquivo, mas antes apaga todos os dados que estavam armazenados ali anteriormente;
* r  — abre um arquivo no modo somente leitura;
* a — grava dados no final do arquivo, sem remover nada do que já estava nele;
* rb — abre um arquivo não textual para leitura;
* wb — abre um arquivo não textual para gravação '''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

   
@bot.command('meme')
async def meme(ctx):
    img_name = random.choie(os.listdir('images'))
    

    with open(f'images/{img_name}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture) 
    
bot.run("Token")