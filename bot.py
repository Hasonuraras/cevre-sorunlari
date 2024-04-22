import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def çevre_sorunu(ctx):
    await ctx.send(f'Su sorunları için $su sorunları-Kirlilik için $kirlilik yazın')

@bot.command()
async def su_sorunlari(ctx):
    await ctx.send(f'Su sorunları milyonlarca insanı  etkiler bu sorunları azaltmak için yapabileceğimiz şeyler çoktur.Mesala denize çöp dökmeyerek, nehirleri kirletmeyerek ve su israf etmeyerek bu sorunları azaltabiliriz. ')

@bot.command()
async def kirlilik(ctx):
    await ctx.send(f'Kirlilik tüm dünyada bulunan bir sorundur.Kirliliği önlemek için Geri dönüşümü destekleyip yere çöp atmamalıyız')



bot.run("")
