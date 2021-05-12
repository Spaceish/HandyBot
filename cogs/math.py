import discord
from discord.ext import commands
import math

class Math(commands.Cog):

    def __init__(self, handy):
        self.handy = handy

    @commands.command()
    async def sum(self, ctx, a : float, b : float):
        await ctx.send(f'**First number : {a}**\n**Second number : {b}**\n**The result : {sum(a, b)}**')
    @commands.command()
    async def mul(self, ctx, a : float, b : float):
        await ctx.send(f'**First number : {a}**\n**Second number : {b}**\n**The result : {mul(a, b)}**')
    @commands.command()
    async def sub(self, ctx, a : float, b : float):
        await ctx.send(f'**First number : {a}**\n**Second number : {b}**\n**The result : {sub(a, b)}**')
    @commands.command()
    async def div(self, ctx, a : float, b : float):
        try:
            await ctx.send(f'**First number : {a}**\n**Second number : {b}**\n**The result : {div(a, b)}**')
        except ZeroDivisionError:
            await ctx.send(f'**First number : {a}**\n**Second number : {b}**\n**Cannot divide with 0.You are playing with fire!**')


def setup(handy):
    handy.add_cog(Math(handy))

def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def pow(a, pow):
    return math.pow(a, pow)

def sqrt(a):
    return math.sqrt(a)
