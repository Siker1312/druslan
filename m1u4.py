#from settings import settings
import discord
from discord.ext import commands
from bot_logic import *
import os
import requests
import time


import random
# import * - это тоже самое, что перечислить все файлы
#from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

total=0 #мой счёт
v = 0 #противник
balance1=0 #для балика пользователя
coont=0 #для работ где пользователь получит балик
f=True
level=1
expi=0
message=0 #Сколько сообщений я отправил


# Когда бот будет готов, он напишет в консоли свое название!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def smile(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def password(ctx, count = 10):
    await ctx.send(gen_pass(count))

#пока команы сверху не нужны но я их оставлю для примера


@bot.command()
async def help_1(ctx):
    await ctx.send(gen_help())

@bot.command()
async def blackjack(ctx,flag = "yes"):
    global total
    global v
    global f
    # Если после blackjack нашишу yes то получится что я создаю свой счёт и счёт противника, так же проверяю не будет ли эти числа больше 21
   
    if flag == "yes":
        total += random.randint(2,11) 
        if f:
            v += random.randint(2,11)
        await ctx.send(f"Ваш счёт {total}") 
        await ctx.send(f"Счёт противник {v}") 
        if total >=21:
            await ctx.send("Вы проиграли")
            total=0
            v=0
            f=True
        elif v>=21:
            await ctx.send("Вы выиграли")
            total=0
            v=0
            f=True
        elif v>=17 and v<=21:
            await ctx.send("Противник остановил ход")
            f=False
        else: 
            
            await ctx.send("Если хотите продолжин введите - $blackjack yes, если остановиться $blackjack no")

    if flag == "no":
        if v>=total:
            await ctx.send(f"Вы проиграли, счёт противник {v}, ваш счёт {total}")
           
        elif total>=v:
            await ctx.send(f"Вы выиграли, ваш счёт {total}, счёт противника {v}")
        total=0
        v=0
        f=True


@bot.command()
async def balance(ctx):
    await ctx.send(f"Твой баланс = {balance1}")

@bot.command()
async def profile(ctx):
    emb=discord.Embed(
        title=f"Здраствуй!",
        description=f"**Баланс** = {balance1}\n**Уровень** = {level}\n**Сообщений** = {message}\n\nДо работы 'Програмист' вам осталось {gen_time1}\nДо работы 'Охраник' вам осталось {gen_time1}\nДо работы 'Босс' вам осталось {gen_time1}"
    )
    await ctx.send(embed=emb)

@bot.command()
async def work(ctx, rabota="ff"):
    global coont
    global balance1
    global f
    if rabota == "ff" and f:
        emb = discord.Embed(
            title="На какую работу вы хотите устроится?",
            description=f'Програмист\nОхраник\nБосс\n\nНапишите - $work (работу на которую хотите, например "Програмист")'
        )
        await ctx.send(embed=emb)
    if rabota == "Програмист":
        if gen_time1.my_time < 1:
            coont +=random.randint(251,301)

            emb= discord.Embed(
                title='Зарплата',
                description=f'__{ctx.author.mention}__, вы получили свои {coont} монет!\n Приходите через 3 часа.'
            )
            await ctx.send(embed=emb)
            balance1+=coont
            coont=0
            f=False
        if gen_time1.my_time>1:
            emb = discord.Embed(
                description=f"Подожди, ты слишком устал!\nПриходи на работу через {gen_time1}"
            )
            await ctx.send(embed=emb)
            f=False

        
    
    if rabota == "Охраник":
        coont +=random.randint(101,151)
        emb = discord.Embed(
            title='Зарплата',
            description=f'__{ctx.author.mention}__, вы получили свои {coont} монет!\n Приходите через 12 часов.'
        )
        await ctx.send(embed=emb)
        balance1+=coont
        coont=0
        f=False
  
    
    
    if rabota == "Босс":
        coont +=random.randint(501,601)
        emb= discord.Embed(
            title='Зарплата',
            description=f'__{ctx.author.mention}__, вы получили свои {coont} монет!\n Приходите через 12 часов.'
        )
        await ctx.send(embed=emb)
        balance1+=coont
        coont=0
        f=False 

@bot.command(
    aliases=["Награда"]
)
async def timely(self,ctx):
    abalance=self.collection.find_one({"_id": ctx.author.id})["balance"]
    self.collection.update_one({"_id": ctx.author.id},
        {"$set": {"balance": abalance + 30}})
    
    emb = discord.Embed(
        title='Временая награда',
        description=f'__{ctx.author.mention}__, вы получили свои 30 монет!\n Приходите через 12 часов.'
    )
    emb.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


bot.run("MTA5MjQ2MTU5NDcyNzk2MDY2Nw.GUaApS.-0Hm4oaAOg4dXGZ5UrIsI3eTdownBfPDKXMzoQ")



