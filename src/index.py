import collections
import discord
from discord.ext import commands
from discord.utils import get
import config
import datetime
import asyncio



api_key = config.api_key
guild_id = config.guild_id





#Command type: >test
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

bot.active = False

bot.today= datetime.date.today()
bot.nextWeek = bot.today + datetime.timedelta(days=-bot.today.weekday(), weeks=1)
bot.actualWeek = bot.today + datetime.timedelta(days=-bot.today.weekday())
bot.lastWeek = bot.actualWeek - datetime.timedelta(days=7)

bot.limpieza = collections.deque(["Baño", "Salon y Pasillo", "Cocina"])
bot.guille = 0
bot.mauri = 1
bot.oscar = 2

def updateDates(self):
    bot.today= datetime.date.today()
    bot.nextWeek = bot.today + datetime.timedelta(days=-bot.today.weekday(), weeks=1)
    bot.actualWeek = bot.today + datetime.timedelta(days=-bot.today.weekday())
    bot.lastWeek = bot.actualWeek - datetime.timedelta(days=7)

def updateToday():
    bot.today= datetime.date.today()


@bot.event
async def on_ready():
    print("BotReady")
    

    #users = discord.Guild.users
    #roles = discord.Guild.roles
    #guild = bot.get_guild(id=guild_id)
    #members = guild.members
    #print(guild.roles)
    #async for member in guild.fetch_members(limit=150):
    #    if not member.bot  and list(guild.roles)[1] in member.roles:
    #        print(member.name)
    #        print(member.roles)

@bot.command()
async def stop(ctx):
    bot.active = False


@bot.command()
async def start(ctx):
    bot.active = True
    await ctx.send('Starting Routine')
    print(bot.active)
    while True:
        if bot.active:
            await asyncio.sleep(5)
            updateToday()
            if bot.today > bot.nextWeek:
                bot.limpieza.rotate()
                channel = bot.get_channel(882606921780199481)
                await channel.send("Gillermo Puto te toca limpiar" + [bot.guillermo])
                await channel.send("Oscar Puto te toca limpiar" + [bot.oscar])
                await channel.send("Mauricio hoy no te toca limpiar nada (" + [bot.mauri] + ")")
        else:
            break

@bot.command()
async def test(ctx):
    print("Online")
    await ctx.send('the bot works correct')

bot.run(api_key)