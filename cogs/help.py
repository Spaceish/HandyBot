import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, handy):
        self.handy = handy

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.blurple()
        )

        embed.set_author(name="Help")
        help_command = {
            "help" : "Shows this message"
        }

        cat = {
            "cfacts" : "Facts about cats."
        }

        math = {
            "sum" : "Sum of two numbers",
            "min" : "Difference between two numbers",
            "mul" : "Multiply two numbers",
            "div" : "Divide two numbers"
        }


        music = {
            "play" : "Play music from a url or keyword",
            "join" : "Join a channel",
            "leave" : "Leave the channel",
            "stop" : "Stops the music",
            "pause" : "Pauses the music",
            "resume" : "Resumes the music"
        }

        def render(commands_dict):
            for command in list(commands_dict):
                embed.add_field(name=command, value=commands_dict.pop(command), inline=False)

        render(help_command)
        render(cat)
        render(math)
        render(music)

        await ctx.send(embed=embed)


def setup(handy):
    handy.add_cog(Help(handy))
