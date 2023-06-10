# ---------------------------------------------------- LUNA✱BOT --------------------------------------------------------
"""
This is a bot file of LUNA✱ Discord Bot Created by Andrew
"""
# ----------------------------------------------------- Libraries ------------------------------------------------------
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
import gtts
from gtts import gTTS
import logging


def luna_bot():
    # ----------------------------------------------- Custom prefixes setup --------------------------------------------
    def get_prefix(client, message):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

# ------------------------------------------ Setup for the Discord Bot client ------------------------------------------
    logging.basicConfig(level=logging.FATAL)
    logger = logging.getLogger('nextcord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename='logs.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    intents = nextcord.Intents().all()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix=get_prefix, intents=intents)
    bot.remove_command("help")

# --------------------------------------------------- Uptime Counter ---------------------------------------------------
    @tasks.loop(seconds=2.0)
    async def uptimeCounter():
        global us, um, uh, ud
        us += 2
        if us == 60:
            us = 0
            um += 1
            if um == 60:
                um = 0
                uh += 1
                if uh == 24:
                    uh = 0
                    ud += 1

    @uptimeCounter.before_loop
    async def beforeUptimeCounter():
        await bot.wait_until_ready()

# ------------------------------------------------------ Cogs ----------------------------------------------------------
    extensions = [
        "cogs.anime",
        "cogs.fun",
        "cogs.money",
        "cogs.moderational",
        "cogs.food",
        "cogs.music",
        "cogs.astro",
        "cogs.animals",
        "cogs.air",
        "cogs.movies",
        "cogs.cars",
        "cogs.voice",
        "cogs.errors",
        "cogs.books",
        "cogs.game",
        "cogs.other"
    ]

    @bot.command()
    @commands.is_owner()
    async def load(ctx, *, cog=None):
        memberid = ctx.author.id
        if memberid == 782956226500755466:
            if cog is None:
                for ext in extensions:
                    bot.load_extension(ext)
                print(Fore.GREEN + f"{seperator}")
                print(Fore.GREEN + f"All Cogs have been loaded successfully! *by command*")
                print(Fore.GREEN + f"On {now}")
                print(Fore.GREEN + f"{seperator}")
                embed = nextcord.Embed(title=f':green_circle: All cogs loaded successfully!',
                                       description=f'```Loaded all extensions```', timestamp=ctx.message.created_at,
                                       color=lunablue)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f':green_circle: Cog loaded successfully!',
                                       description=f'```Loaded {cog} extension```', timestamp=ctx.message.created_at,
                                       color=lunablue)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                print(Fore.GREEN + f"{seperator}")
                print(Fore.GREEN + f"cogs.{cog} Cog has been loaded successfully! *By command*")
                print(Fore.GREEN + f"On {now}")
                print(Fore.GREEN + f"{seperator}")
                bot.load_extension("cogs." + cog)
        else:
            embed = nextcord.Embed(title=f'Only my creator can load/unload extensions.',
                                   description=f'{ctx.author} Why are you even trying...',
                                   timestamp=ctx.message.created_at,
                                   color=lunablue)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            print(Fore.YELLOW + f"{seperator}")
            print(Fore.YELLOW + "Someone tried to use .unload... i wont let them.")
            print(Fore.YELLOW + f"{seperator}")

    @bot.command()
    @commands.is_owner()
    async def unload(ctx, *, cog=None):
        memberid = ctx.author.id
        if memberid == 782956226500755466:
            if cog is None:
                for ext in extensions:
                    bot.unload_extension(ext)
                print(Fore.GREEN + f"{seperator}")
                print(Fore.GREEN + f"All Cogs have been unloaded successfully! *by command*")
                print(Fore.GREEN + f"On {now}")
                print(Fore.GREEN + f"{seperator}")
                embed = nextcord.Embed(title=f':red_circle: All cogs unloaded successfully!',
                                       description=f'```Unloaded all extensions```', timestamp=ctx.message.created_at,
                                       color=lunablue)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f':red_circle: Cog unloaded successfully!',
                                       description=f'```Unloaded {cog} extension```', timestamp=ctx.message.created_at,
                                       color=lunablue)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                print(Fore.GREEN + f"{seperator}")
                print(Fore.GREEN + f"cogs.{cog} Cog has been unloaded successfully! *By command*")
                print(Fore.GREEN + f"On {now}")
                print(Fore.GREEN + f"{seperator}")
                bot.unload_extension("cogs." + cog)
        else:
            embed = nextcord.Embed(title=f'Only my creator can load/unload extensions.',
                                   description=f'{ctx.author} Why are you even trying...',
                                   timestamp=ctx.message.created_at,
                                   color=lunablue)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            print(Fore.YELLOW + f"{seperator}")
            print(Fore.YELLOW + "Someone tried to use .unload... i wont let them.")
            print(Fore.YELLOW + f"{seperator}")

    @bot.command()
    @commands.is_owner()
    async def reload(ctx, *, cog=None):
        memberid = ctx.author.id
        if memberid == 782956226500755466:
            if cog is None:
                for ext in extensions:
                    bot.unload_extension(ext)
                    bot.load_extension(ext)
                print(Fore.GREEN + f"{seperator}")
                print(Fore.GREEN + f"All Cogs have been reloaded successfully! *by command*")
                print(Fore.GREEN + f"On {now}")
                print(Fore.GREEN + f"{seperator}")
                embed = nextcord.Embed(title=f':arrows_clockwise: All cogs reloaded successfully!',
                                       description=f'```Reloaded all extensions```', timestamp=ctx.message.created_at,
                                       color=lunablue)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f':arrows_clockwise: Cog reloaded successfully!',
                                       description=f'```Reloaded {cog} extension```', timestamp=ctx.message.created_at,
                                       color=lunablue)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                print(Fore.GREEN + f"{seperator}")
                print(Fore.GREEN + f"cogs.{cog} Cog has been reloaded successfully! *By command*")
                print(Fore.GREEN + f"On {now}")
                print(Fore.GREEN + f"{seperator}")
                bot.unload_extension("cogs." + cog)
                bot.load_extension("cogs." + cog)
        else:
            embed = nextcord.Embed(title=f'Only my creator can load/unload extensions.',
                                   description=f'{ctx.author} Why are you even trying...',
                                   timestamp=ctx.message.created_at,
                                   color=lunablue)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            print(Fore.YELLOW + f"{seperator}")
            print(Fore.YELLOW + "Someone tried to use .reload... i wont let them.")
            print(Fore.YELLOW + f"{seperator}")

# ---------------------------------------------------- Level System ----------------------------------------------------
    async def update_data(users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 1

    async def add_experience(users, user, exp):
        users[f'{user.id}']['experience'] += exp

    async def level_up(users, user, message):
        with open('levels.json', 'r') as g:
            levels = json.load(g)
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience ** (1 / 4))
        if lvl_start < lvl_end:
            embed = nextcord.Embed(title=f':tada: {user} has leveled up! **[LVL{lvl_end}]**', color=lunablue)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await message.channel.send(embed=embed)
            users[f'{user.id}']['level'] = lvl_end

# ------------------------------------------ On ready function and bot events ------------------------------------------
    @bot.event
    async def on_ready():
        print(Fore.MAGENTA + f"{seperator}")
        print(Fore.WHITE + f"Starting " + Fore.MAGENTA + "LUNA✱" + Fore.WHITE + " Bot...")
        print(Fore.MAGENTA + f"{seperator}")
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.WHITE + f"Attempting to load cogs!")
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.GREEN + f"{seperator}")
        for ext in extensions:
            bot.load_extension(ext)
            print(Fore.WHITE + f"Name: " + Fore.GREEN + f"{ext}" + Fore.WHITE + " Status: " + Fore.GREEN + "loaded")
        print(Fore.GREEN + f"{seperator}")
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.WHITE + f"All cogs loaded successfully!")
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.MAGENTA + f"{seperator}")
        print(Fore.WHITE + f"Logged in as: " + Fore.MAGENTA + f"{bot.user.name}")
        print(Fore.WHITE + f"On: " + Fore.MAGENTA + f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(Fore.WHITE + f"Version number: " + Fore.MAGENTA + f"{version}")
        print(Fore.MAGENTA + f"{seperator}")
        print(Fore.WHITE + f"Python version: " + Fore.MAGENTA + f"{pythonv}")
        print(Fore.WHITE + f"Nextcord version: " + Fore.MAGENTA + f"{nextcordv}")
        print(Fore.MAGENTA + f"{seperator}")

        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing,
                                                             name=f"On {len(bot.guilds)} servers!"),
                                  status=nextcord.Status.online)
        uptimeCounter.start()

    @bot.event
    async def on_member_join(member):
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, member)

        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)

        embed = nextcord.Embed(title=f'Welcome to {member.guild.name}!',
                               description='Hello! I am LUNA and I am helping out on the server you just joined.',
                               color=lunaorange)
        embed.add_field(name='You can use ```.help```', value=f'to view my commands')
        embed.add_field(name=f'Enjoy your stay {member.name}', value=f'on {member.guild.name}')
        embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        embed.set_thumbnail(url="https://i.ibb.co/yBXMVKG/icon.png")
        await member.send(embed=embed)

    @bot.event
    async def on_message(message):
        try:
            if not message.author.bot:
                with open('users.json', 'r') as f:
                    users = json.load(f)

                await update_data(users, message.author)
                await add_experience(users, message.author, 2)
                await level_up(users, message.author, message)

                with open('users.json', 'w') as f:
                    json.dump(users, f, indent=4)

            await bot.process_commands(message)

        except:
            embed = nextcord.Embed(title=f':x: I cant respond to direct messages!',
                                   description='`Try using one of my commands on our mutual guilds`',
                                   color=lunablue)
            embed.add_field(name='You can use ```.help```', value=f'to view my commands on any mutual server')
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            embed.set_thumbnail(url="https://i.ibb.co/yBXMVKG/icon.png")
            await message.author.send(embed=embed)

    @bot.event
    async def on_guild_join(guild):
        print(Fore.GREEN + f"{seperator}")
        print(Fore.GREEN + f"Joined a new server!")
        print(Fore.WHITE + "Name: " + Fore.GREEN + f"{guild.name}")
        print(Fore.WHITE + "On: " + Fore.GREEN + f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(Fore.GREEN + f"{seperator}")

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '.'

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = nextcord.Embed(title=f'Thanks for adding me to {guild.name}!',
                                       description='I am LUNA and I will make your life easier', color=lunaorange)
                embed.add_field(name=f'Use ```.help```', value=f'for the list of commands.', inline=False)
                embed.add_field(name=f'Use ```.serverinfo```', value=f'to display detailed info about this guild.',
                                inline=False)
                embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_thumbnail(url="https://i.ibb.co/yBXMVKG/icon.png")
                await channel.send(embed=embed)
            break

    @bot.event
    async def on_guild_remove(guild):
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.YELLOW + f"Got removed from a server!")
        print(Fore.WHITE + "Name: " + Fore.YELLOW + f"{guild.name}")
        print(Fore.WHITE + "On: " + Fore.YELLOW + f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(Fore.YELLOW + f"{seperator}")

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

#  ------------------------------------------------- Help Command ------------------------------------------------------
    class Dropdown(nextcord.ui.Select):
        def __init__(self):
            options = [
                nextcord.SelectOption(label="Fun Commands", description=" "),
                nextcord.SelectOption(label="Moderational Commands", description=" "),
                nextcord.SelectOption(label="Utility Commands", description=" "),
                nextcord.SelectOption(label="Anime Commands", description=" "),
                nextcord.SelectOption(label="Money Commands", description=" "),
                nextcord.SelectOption(label="Food Commands", description=" "),
                nextcord.SelectOption(label="Music Commands", description=" "),
                nextcord.SelectOption(label="Astro Commands", description=" "),
                nextcord.SelectOption(label="Animals Commands", description=" "),
                nextcord.SelectOption(label="Air Commands", description=" "),
                nextcord.SelectOption(label="Movie Commands", description=" "),
                nextcord.SelectOption(label="Car Commands", description=" "),
                nextcord.SelectOption(label="Voice Commands", description=" "),
                nextcord.SelectOption(label="Book Commands", description=" "),
                nextcord.SelectOption(label="Game Commands", description=" "),
                nextcord.SelectOption(label="Other Commands", description=" ")
            ]
            super().__init__(placeholder='Select help subject', min_values=1, max_values=1, options=options)

        async def callback(self, interaction: nextcord.Interaction):
            if self.values[0] == 'Fun Commands':
                pageNum = 0
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Moderational Commands':
                pageNum = 1
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Utility Commands':
                pageNum = 2
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Anime Commands':
                pageNum = 3
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Money Commands':
                pageNum = 4
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Food Commands':
                pageNum = 5
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Music Commands':
                pageNum = 6
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Astro Commands':
                pageNum = 7
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Animals Commands':
                pageNum = 8
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Air Commands':
                pageNum = 9
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Movie Commands':
                pageNum = 10
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Car Commands':
                pageNum = 11
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Voice Commands':
                pageNum = 12
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Book Commands':
                pageNum = 13
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Game Commands':
                pageNum = 14
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            if self.values[0] == 'Other Commands':
                pageNum = 15
                pageTitle = list(helpGuide)[pageNum]
                embed = nextcord.Embed(title=f"{pageTitle}", color=lunaorange)
                for key, val in helpGuide[pageTitle].items():
                    embed.add_field(name="." + key, value=val, inline=True)
                    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn",
                                     icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                return await interaction.response.send_message(embed=embed)

            await interaction.response.send_message(f'You chose {self.values[0]}')

    class DropdownView(nextcord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(Dropdown())

    @bot.command(aliases=['?', 'h'])
    async def help(ctx):
        view = DropdownView()
        embed = nextcord.Embed(title=':grey_question: Welcome to LUNA✱ help panel!',
                               description=':information_source: Please select category from the dropdown menu below.',
                               color=lunaorange)
        embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        embed.set_thumbnail(url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed, view=view)

#  ------------------------------------------------ Other Commands -----------------------------------------------------
    @bot.command()
    async def trivia(ctx, *, category=None):
        if category is None:
            embed = nextcord.Embed(title=f":grey_question: Please choose a category",
                                   description=f"Type .trivia [category] to start!",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="Categories:", value=f"`artliterature` `language`", inline=False)
            embed.add_field(name="", value=f"`sciencenature` `general`", inline=False)
            embed.add_field(name="", value=f"`food-drink` `peopleplaces`", inline=False)
            embed.add_field(name="", value=f"`geography` `historyholidays`", inline=False)
            embed.add_field(name="", value=f"`entertainment` `toysgames`", inline=False)
            embed.add_field(name="", value=f"`music` `mathematics`", inline=False)
            embed.add_field(name="", value=f"`religionmythology` `sportsleisure`", inline=False)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        else:
            api = f"https://api.api-ninjas.com/v1/trivia?category={category}"
            response = requests.get(api, headers={"X-Api-Key": NINJAS_KEY}).json()
            data = response[0]
            category = data["category"]
            question = data["question"]
            answer = data["answer"].lower()
            print(Fore.MAGENTA + f"{seperator}")
            print(Fore.MAGENTA + f"Correct answer for trivia: {answer}")
            print(Fore.MAGENTA + f"On {now} for {ctx.author}")
            print(Fore.MAGENTA + f"{seperator}")
            embed = nextcord.Embed(title=f":grey_question: Here's a trivia about `{category}`",
                                   description=f"You have 60 seconds to give an answer. Type `give up` to see the answer",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="Category:", value=f"{category}", inline=False)
            embed.add_field(name="Question:", value=f"{question}", inline=False)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

            try:
                msg = await bot.wait_for('message', timeout=60, check=lambda message: message.author == ctx.author)
            except asyncio.TimeoutError:
                await ctx.send("You took too long to answer, try again!")
                return

            if msg.content == answer:
                embed = nextcord.Embed(title=f":green_circle: Correct!",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                return

            if msg.content == "give up":
                embed = nextcord.Embed(title=f":red_circle: You gave up!",
                                       description=f"Correct answer:",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name=f"{answer}", value="")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)

            else:
                embed = nextcord.Embed(title=f":red_circle: Wrong try again!",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                return

    @bot.command()
    async def riddle(ctx):
        api = "https://api.api-ninjas.com/v1/riddles"
        response = requests.get(api, headers={"X-Api-Key": NINJAS_KEY}).json()
        data = response[0]
        title = data["title"]
        question = data["question"]
        answer = data["answer"].lower()
        print(Fore.MAGENTA + f"{seperator}")
        print(Fore.MAGENTA + f"Correct answer for a riddle: {answer}")
        print(Fore.MAGENTA + f"On {now} for {ctx.author}")
        print(Fore.MAGENTA + f"{seperator}")

        embed = nextcord.Embed(title=f":grey_question: Here's a riddle:",
                               description=f"You have 60 seconds to give an answer. Type `give up` to see the answer. NOTE: Add '.' on the end of your answer to register properly!",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.add_field(name="TItle:", value=f"{title}", inline=False)
        embed.add_field(name="Riddle:", value=f"{question}", inline=False)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

        try:
            msg = await bot.wait_for('message', timeout=60, check=lambda message: message.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to answer, try again!")
            return

        if msg.content == answer:
            embed = nextcord.Embed(title=f":green_circle: Correct!",
                                   description=f"",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            return

        if msg.content == "give up":
            embed = nextcord.Embed(title=f":red_circle: You gave up!",
                                   description=f"Correct answer:",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name=f"{answer}", value="")
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            return

        else:
            embed = nextcord.Embed(title=f":red_circle: Wrong try again!",
                                   description=f"",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

    # -------------------------------------------------- Running the bot -----------------------------------------------
    bot.run(token)
