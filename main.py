import discord
import os
import requests
import random
from discord.ext import commands
from model import detect

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def call1(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def call2(ctx, a: int, b: int):
    await ctx.send(a - b)

@bot.command()
async def call3(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command()
async def call4(ctx, a: int, b: int):
    await ctx.send(a // b)

@bot.command()
async def callt(ctx, a: int, b: int):
    await ctx.send(a / b)

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def meme(ctx):
    all_mems = os.listdir("images")
    rand_mem = random.choice(all_mems)
    with open(f"images/{rand_mem}", 'rb') as f:
        imagesd = discord.File(f)
    await ctx.send(file=imagesd)

@bot.command()
async def ameme(ctx):
    all_amems = os.listdir("Ameme")
    rand_amem = random.choice(all_amems)
    with open(f"Ameme/{rand_amem}", 'rb') as f:
        Ameme = discord.File(f)
    await ctx.send(file=Ameme)

@bot.command()
async def detect_b(ctx):
    if ctx.message.attachments:
        numberi = 1
        for i in ctx.message.attachments:
            url = i.url
            name = i.filename
            await i.save(f'./{name}')
            q = detect(image = f'./{name}', model = './keras_model.h5', txtt = './labels.txt')
            simvols = '''\\n'''
            for i in simvols:
                classn = q[0].replace(i, '')
            vera = q[2]
            index = q[1] 
            await ctx.send(f'Изображение {numberi}')
            await ctx.send(f'Найденный класс: {classn}')
            await ctx.send(f'Вероятность: {vera}')
            if index == 0:
                await ctx.send('''Всего в мире существует 35 видов голубей.
                         Самым распространённым из них является сизый,
                         именно этих птиц вы можете увидеть у себя за окном.''')

            elif index == 1:
                await ctx.send('''Многие думают, что свое название птица получила вследствие синего окраса перьев. Однако синее оперение почти не характерно для синиц.
                В действительности, их стали так называть в связи со звуками, которые они издают. Если прислушаться, то можно расслышать нечто похожее на «си-синь-си».''')

            elif index == 2:
                await ctx.send('''У попугаев отлично развито чувство ритма
              — они могут действительно ритмично танцевать под музыку.''')

            elif index == 3:
                await ctx.send('''Всего в мире существует 35 видов голубей.
                         Самым распространённым из них является сизый,
                         именно этих птиц вы можете увидеть у себя за окном.''')

            await ctx.send('''--------------------------------------------------''')
            numberi += 1
    else:
        await ctx.send('Чё-то не получилось попробуйте с картинкой.')

bot.run("HERE THE TOKEN")