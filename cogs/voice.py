"""
This is a cog file of LUNA✱ Containing voice commands
"""
import nextcord
from nextcord.ext import commands, tasks
from config.colors import *
from config.config import *
import json
from reddit_setup import *
from api_keys import *
import aiohttp
import asyncio
import requests
import pyaztro
import dateutils
import gtts
from gtts import gTTS


class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, ctx, lang, *args):
        text = " ".join(args)
        user = ctx.message.author
        if user.voice is not None:
            try:
                vc = await user.voice.channel.connect()
            except:
                vc = ctx.voice_client

            sound = gTTS(text=text, lang=lang, slow=False)
            sound.save("tts-audio.mp3")

            if vc.is_playing():
                vc.stop()

            source = await nextcord.FFmpegOpusAudio.from_probe("tts-audio.mp3", method="fallback")
            vc.play(source)
        else:
            embed = nextcord.Embed(title=f":red_circle: You need to be in a voice channel to use that!",
                                   description=f"",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

    @commands.command()
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            embed = nextcord.Embed(title=f':x: You are not in a voice channel.', timestamp=ctx.message.created_at,
                                   color=lunaorange)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            return await ctx.send(embed=embed)
        await ctx.author.voice.channel.connect()
        embed = nextcord.Embed(title=f':notes: Joined your voice channel.', timestamp=ctx.message.created_at,
                               color=lunaorange)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=["stop"])
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            embed = nextcord.Embed(title=f':x: You are not in a voice channel.', timestamp=ctx.message.created_at,
                                   color=lunaorange)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            return await ctx.send(embed=embed)
        if mevoicetrue is None:
            embed = nextcord.Embed(title=f':x: I am not in a voice channel.', timestamp=ctx.message.created_at,
                                   color=lunaorange)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            return await ctx.send(embed=embed)
        await ctx.voice_client.disconnect()
        embed = nextcord.Embed(title=f':heavy_multiplication_x: Left the voice channel.',
                               timestamp=ctx.message.created_at,
                               color=lunaorange)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(voice(bot))
