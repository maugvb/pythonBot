import discord
from discord.ext import commands
from discord.utils import get
import config


api_key = config.api_key

#Command type: >test
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="", intents=intents)



@bot.event

async def on_ready():
    print("BotReady")
    #users = discord.Guild.users
    roles = discord.Guild.roles
    guild = bot.get_guild(id=882606921780199475)
    members = guild.members
    print(guild.roles)
    async for member in guild.fetch_members(limit=150):
        if member.name != 'PisoBot' and list(guild.roles)[1] in member.roles:
            print(member.name)
            print(list(guild.roles)[1].name)



@bot.command()
async def test(ctx):
    print("Online")
    await ctx.send('the bot works correct')

bot.run(api_key)