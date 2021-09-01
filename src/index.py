import discord
from discord.ext import commands
import config


api_key = config.api_key
#Command type: >test
bot = commands.Bot(command_prefix=">")


@bot.event
async def on_ready():
    print("BotReady")


@bot.command()
async def test(ctx):
    print("Online")
    await ctx.send('the bot correct')

bot.run(api_key)