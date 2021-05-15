import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

prefix = "^"
handy = commands.Bot(command_prefix=prefix)
handy.remove_command('help')

@handy.event
async def on_ready():
    print('Ready!')

@handy.command()
async def load(ctx, extension):
    handy.load_extension(f'cogs.{extension}')

@handy.command()
async def unload(ctx, extension):
    handy.unload_extension(f'cogs.{extension}')

@handy.command()
async def reload(ctx, extension):
    handy.unload_extension(f'cogs.{extension}')
    handy.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        handy.load_extension(f'cogs.{filename[:-3]}')

token = os.getenv('TOKEN')
handy.run(token)
