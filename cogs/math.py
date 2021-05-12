import discord
from discord.ext import commands
import mathhelper

class Math(commands.Cog):

    def __init__(self, handy):
        self.handy = handy

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')

    @commands.command()
    async def sum(self, ctx, a : float, b : float):
        sum = mathhelper.sum(a, b)
        await ctx.send(sum)

def setup(handy):
    handy.add_cog(Math(handy))
