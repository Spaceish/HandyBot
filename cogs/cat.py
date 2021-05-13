import discord
from discord.ext import commands
import random
import requests

class Cat(commands.Cog):

    def __init__(self, handy):
        self.handy = handy
        ids = []

    @commands.command()
    async def cfacts(self, ctx):
        await ctx.send(f'**Fact :** {catfacts()}')

def setup(handy):
    handy.add_cog(Cat(handy))

def catfacts():
    ids = ["58e008800aac31001185ed07", "58e008630aac31001185ed01", "58e00a090aac31001185ed16", "58e009390aac31001185ed10", "58e008780aac31001185ed05"]
    id = random.choice(ids)
    fact = requests.get(f'https://cat-fact.herokuapp.com/facts/{id}')

    return fact.json()['text']
