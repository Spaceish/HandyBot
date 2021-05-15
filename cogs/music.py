import discord
from discord.ext import commands
import youtube_dl
import os

staff = ["Zeno#7226", "SpaceDot.#7662"]

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}



ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

class Music(commands.Cog):
    def __init__(self, handy):
        self.handy = handy

    @commands.command()
    async def play(self, ctx, url):
        try:
            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                filename = await YTDLSource.from_url(url, loop=self.handy.loop)
                voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
            await ctx.send(f'**Playing : {filename}**')
        except Exception as e:
                await ctx.send(f"**Exception : {e}**")
    @commands.command()
    async def local_play(self, ctx, filename):
            try:
                server = ctx.message.guild
                voice_channel = server.voice_client

                async with ctx.typing():
                    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
                await ctx.send(f'**Playing : {filename}**')
            except Exception as e:
                    if ctx.message.author not in staff:
                        await ctx.send(f"**Exception : Dev only command({staff[0]}, {staff[1]}).**")
                    else:
                        await ctx.send(f"**Exception : {e}**")

    @commands.command()
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send(f"**Exception : You aren't in a voice channel**")
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()
    @commands.command()
    async def pause(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send(f"**Exception : I'm wasn't playing anything.**")
    @commands.command()
    async def resume(self, ctx):
            voice_client = ctx.message.guild.voice_client
            if voice_client.is_paused():
                await voice_client.resume()
            else:
                await ctx.send(f"**Exception : The music was not paused.**")
    @commands.command()
    async def stop(self, ctx):
            voice_client = ctx.message.guild.voice_client
            if voice_client.is_playing():
                await voice_client.stop()
            else:
                await ctx.send("**Exception : I'm not playing anything**")
    @commands.command()
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("**Exception : I'm not connected to any voice channel**")

def setup(handy):
    handy.add_cog(Music(handy))
