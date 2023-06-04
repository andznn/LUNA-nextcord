"""
This is a cog file of LUNA✱ Containing error handling
"""
import nextcord
from nextcord.ext import *
from nextcord import *
import json
import random
import datetime
import colorama
from colorama import Fore, Style
import sys
from bot_token import token
from reddit_setup import *
from config.colors import lunaorange, lunablue
from api_keys import *
import aiohttp
import asyncio
from config.config import *
import requests
import dateutils
import os
import wikipedia
import time
import gtts
from gtts import gTTS

bot_user_name = "LUNA✱"

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(title=f":no_entry: You don't have permissions to perform that.",
                                   description=f"```[{str(error)}]```", color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandNotFound):
            embed = nextcord.Embed(title=f":x: There is no such command!", description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(title=f":x: Command is missing required arguments.",
                                   description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.ExtensionError):
            embed = nextcord.Embed(title=f":x: Extension error", description=f"```[{str(error)}]```", color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BotMissingRole):
            embed = nextcord.Embed(title=f":x: I am missing a required role to do that!",
                                   description=f"```[{str(error)}]```", color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BotMissingPermissions):
            embed = nextcord.Embed(title=f":x: I am missing permissions to do that",
                                   description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.ChannelNotFound):
            embed = nextcord.Embed(title=f":question: Channel not found or not readable",
                                   description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandOnCooldown):
            embed = nextcord.Embed(title=f":clock1: Command on cooldown, please wait",
                                   description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.DisabledCommand):
            embed = nextcord.Embed(title=f":x: Command temporarily disabled.", description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MemberNotFound):
            embed = nextcord.Embed(title=f":question: Member not found", description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.TooManyArguments):
            embed = nextcord.Embed(title=f":1234: Too many arguments, please try again!",
                                   description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.NSFWChannelRequired):
            embed = nextcord.Embed(title=f":x: Restricted to NSFW channels!", description=f"```[{str(error)}]```",
                                   color=lunablue)
            embed.set_footer(text=f"{bot_user_name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandError):
            print(Fore.RED + f"{seperator}")
            print(Fore.WHITE + f"Error raised by: " + Fore.RED + f"{ctx.author.name} ({ctx.author.mention})")
            print(Fore.WHITE + f"Error message: " + Fore.RED + f"{error}")
            print(Fore.WHITE + f"On: " + Fore.RED + f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(Fore.RED + f"{seperator}")

def setup(bot: commands.Bot):
    bot.add_cog(errors(bot))
