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
    @commands.command()
    async def sqrt(self, ctx, a : float):
        try:
            await ctx.send(f'**Number : {a}**\n**The result : {sqrt(a)}**')
        except ValueError:
            await ctx.send(f'**Number : {a}**\n**Exception : Cannot get the square root of negative numbers.(Bot cannot handle complex math yet so, this is limited to basic math.)**')
    @commands.command()
    async def pow(self, ctx, a : float, power : float):
        await ctx.send(f'**Number : {a}**\n**Power : {b}**\n**The result : {pow(a, power)}**')


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
