import discord
from discord.ext import commands
import math
import requests

class Conversions(commands.Cog):

    def __init__(self, handy):
        self.handy = handy

        @commands.command()
        async def convert(self, ctx, type, another_type, value):
            await ctx.send(convert(type, another_type, value))

def setup(handy):
    handy.add_cog(Conversions(handy))

def convert(type, another_type, value):
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"

    querystring = {"format":"json","from":type,"to":another_type,"amount":value}

    headers = {
        'x-rapidapi-key': "SIGN-UP-FOR-KEY",
        'x-rapidapi-host': "currency-converter5.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text
