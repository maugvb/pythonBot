import discord
from discord.ext import commands
from discord.utils import get
import config


api_key = config.api_key
guild_id = config.guild_id

#Command type: >test
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="", intents=intents)



@bot.event

async def on_ready():
    print("BotReady")
    #users = discord.Guild.users
    roles = discord.Guild.roles
    guild = bot.get_guild(id=guild_id)
    members = guild.members
    print(guild.roles)
    async for member in guild.fetch_members(limit=150):
        if not member.bot  and list(guild.roles)[1] in member.roles:
            print(member.name)
            print(member.roles)



@bot.command()
async def test(ctx):
    print("Online")
    await ctx.send('the bot works correct')

bot.run(api_key)