import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, ctx):

        cat = {
            commands : ["cfacts"]
        }

        math = {
            commands : ["sum", ""]
        }


def setup(handy):
    handy.add_cog(Help(handy))
