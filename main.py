# ---------------------------------------------------- LUNA✱BOT --------------------------------------------------------
"""
This is a main file of LUNA✱ Discord Bot Created by Andrew
Current version: v1.2/2023
Newest added functionality: Added errors cog and error handling in cogs + books searching commands
Updated: 04.06.2023
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
import time
import gtts
from gtts import gTTS


# ----------------------------------------------- Custom prefixes setup ------------------------------------------------
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


# ------------------------------------------ Setup for the Discord Bot client ------------------------------------------
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
    "cogs.books"
]

if __name__ == "__main__":
    print(Fore.MAGENTA + f"{seperator}")
    print(Fore.WHITE + f"Starting " + Fore.MAGENTA + "LUNA✱" + Fore.WHITE + " Bot...")
    print(Fore.MAGENTA + f"{seperator}")
    time.sleep(0.25)
    print(Fore.YELLOW + f"{seperator}")
    print(Fore.WHITE + f"Attempting to load cogs!")
    print(Fore.YELLOW + f"{seperator}")
    time.sleep(0.25)
    print(Fore.GREEN + f"{seperator}")
    time.sleep(0.25)
    for ext in extensions:
        bot.load_extension(ext)
        print(Fore.WHITE + f"Name: " + Fore.GREEN + f"{ext}" + Fore.WHITE + " Status: " + Fore.GREEN + "loaded")
        time.sleep(0.25)
    time.sleep(0.25)
    print(Fore.GREEN + f"{seperator}")
    time.sleep(0.25)
    print(Fore.YELLOW + f"{seperator}")
    print(Fore.WHITE + f"All cogs loaded successfully!")
    print(Fore.YELLOW + f"{seperator}")


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
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
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


#  --------------------------------------------------- Help Command ----------------------------------------------------
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

        if self.values[0] == 'Other Commands':
            pageNum = 14
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


#  --------------------------------------------- Utility & Other Commands ----------------------------------------------
@bot.command(aliases=['logoff', 'terminate'], hidden=True)
@commands.is_owner()
async def shutdown(ctx, interaction: Interaction):
    memberid = ctx.author.id
    if memberid == 782956226500755466:
        embed = nextcord.Embed(title=f':red_circle: My code has been terminated. Shutting down...',
                               description=f'```Hope to see you back soon```', timestamp=ctx.message.created_at,
                               color=lunablue)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.YELLOW + "Shutdown by command. Turning off...")
        print(Fore.YELLOW + f"{seperator}")
        await asyncio.sleep(3)
        await bot.close()
    else:
        embed = nextcord.Embed(title=f'Only my creator can shut me down.',
                               description=f'{ctx.author} Why are you even trying...',
                               timestamp=ctx.message.created_at,
                               color=lunablue)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)
        print(Fore.YELLOW + f"{seperator}")
        print(Fore.YELLOW + "Someone tried to shut me down... i wont let them.")
        print(Fore.YELLOW + f"{seperator}")


@bot.command(description="Disables selected command")
@commands.has_permissions(administrator=True)
async def toggle(ctx, *, command):
    try:
        command = bot.get_command(command)
        if ctx.command == command:
            embed = nextcord.Embed(title=f':x: You cannot disable this command.', color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            embed = nextcord.Embed(title=f':ballot_box_with_check: I {ternary} {command.qualified_name}',
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
    except AttributeError:
        embed = nextcord.Embed(title=f":x: Couldn't find that command",
                               description=f'Please try again!',
                               color=lunablue, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)


@bot.command(aliases=["statistics", "uptime"])
@commands.has_permissions(administrator=True)
async def stats(ctx):
    global us, um, uh, ud
    embed = nextcord.Embed(title='My Stats', description='Uptime:', timestamp=ctx.message.created_at, color=lunaorange)
    embed.add_field(name=f"Days: ", value=ud, inline=False)
    embed.add_field(name=f"Hours: ", value=uh, inline=False)
    embed.add_field(name=f"Minutes: ", value=um, inline=False)
    embed.add_field(name=f"Seconds: ", value=us, inline=False)
    embed.add_field(name=f"Name: ", value=f"{bot.user.name}")
    embed.add_field(name=f"Creator: ", value=f"{creator}")
    embed.add_field(name=f"Version: ", value=f"{version}")
    embed.add_field(name=f"Nextcord: ", value=f"{nextcordv}")
    embed.add_field(name=f"Python: ", value=f"{pythonv}")
    embed.add_field(name=f"Help Panel: ", value=f"Use .help")
    embed.add_field(name=f"Based on Nextcord", value=f"https://docs.nextcord.dev/en/stable/", inline=False)
    embed.add_field(name=f"GitHub Repository", value=f"https://github.com/andzn986/LUNA-nextcord/", inline=False)
    embed.set_image(url="https://i.ibb.co/jrNLFw2/lunatrans.png")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
    await ctx.send(embed=embed)


@bot.command(aliases=["inv"])
@commands.has_permissions(create_instant_invite=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def invite(ctx):
    invite = await ctx.guild.text_channels[0].create_invite(max_age=0, max_uses=0)
    embed = nextcord.Embed(title=f":envelope_with_arrow: Success!",
                           description=f"Here's your invite {ctx.author.mention}", color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
    await ctx.send(embed=embed)
    await ctx.send(invite)


@bot.command(aliases=['lvl', 'exp'], description="Displays users level")
@commands.cooldown(1, 10, commands.BucketType.user)
async def level(ctx, member: nextcord.Member = None):
    try:
        if not member:
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(ctx.message.author.id)]['level']
            embed = nextcord.Embed(title=f':bust_in_silhouette: You are at level {lvl}!', color=lunablue,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        if member.id == 1108328414823317504:
            embed = nextcord.Embed(title=f"I don't have a level!", color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        else:
            id = member.id
            with open('users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            embed = nextcord.Embed(title=f':bust_in_silhouette: {member} is at level {lvl}!', color=lunablue,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
    except AttributeError:
        pass


@bot.command(aliases=['remind', 'reminder', 'tr'], description="Sets a timer with a reminder")
async def timer(ctx, seconds, *, reminder):
    try:
        secondint = int(seconds)
        if secondint > 300:
            embed = nextcord.Embed(title=f":x: Can't go over 5 minutes.", color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            raise BaseException
        if secondint <= 0:
            embed = nextcord.Embed(title=f":x: Number cannot be negative.", color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            raise BaseException

        message = await ctx.send(f':timer: Timer: {seconds}')

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content=':timer: Timer ended!')
                break

            await message.edit(content=f':timer: Timer: {secondint}')
            await asyncio.sleep(1)

        embed = nextcord.Embed(title=f"{reminder}", description=f':timer: Your timer has ended.', color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(f"{ctx.author.mention}", embed=embed)
    except ValueError:
        embed = nextcord.Embed(title=f":x: Missing argument. You must enter a number.", color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)


@bot.command(aliases=["version", "v"], description="Displays current bot version")
async def ver(ctx):
    embed = nextcord.Embed(title=f":globe_with_meridians: LUNA✱",
                           description=f"```Version: {version}, Created by: {creator}```", color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command(aliases=["repeat"], description="Repeats users message")
@commands.has_permissions(send_messages=True)
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f"{text}")


@bot.command(aliases=["shout"], description="Announces users message with @ everyone tag")
@commands.has_permissions(mention_everyone=True)
async def announce(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f"@everyone")
    embed = nextcord.Embed(title=f":mega: {text}", description=f"Announcement by {ctx.author.mention}",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command(aliases=["latency"], description="Displays bot latency")
async def ping(ctx):
    latency = bot.latency
    embed = nextcord.Embed(
        title=":inbox_tray: Pong! Here's my latency:",
        description=f'**{latency * 1000:.2f}ms**',
        color=lunaorange
    )
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
    await ctx.send(embed=embed)


@bot.command(aliases=["pic", "pfp"], description="Sends users avatar")
async def avatar(ctx, *, member: nextcord.Member = None):
    if member == None:
        member = ctx.author

    memberAvatar = member.avatar.url

    embed = nextcord.Embed(title=f"{member}'s avatar:", description=f"{member.mention}", color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.set_image(url=memberAvatar)
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command(aliases=["si", "info", "server"], description="Displays current server info")
async def serverinfo(ctx):
    global bot
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

    embed = nextcord.Embed(title=f':information_source: Server Info: {ctx.guild.name}',
                           timestamp=ctx.message.created_at,
                           color=lunaorange)
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name='Name', value=f'{ctx.guild.name}', inline=False)
    embed.add_field(name='Description', value=f'{ctx.guild.description}', inline=False)
    embed.add_field(name='Server ID', value=f'{ctx.guild.id}', inline=False)
    embed.add_field(name='Owner', value=f'{ctx.guild.owner}', inline=False)
    embed.add_field(name='Region', value=f'{ctx.guild.region}', inline=False)
    embed.add_field(name='Members', value=ctx.guild.member_count, inline=False)
    embed.add_field(name='Verification level', value=str(ctx.guild.verification_level), inline=False)
    embed.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
    embed.add_field(name='Role count', value=str(role_count), inline=False)
    embed.add_field(name='Bots', value=', '.join(list_of_bots), inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def profile(ctx, user: nextcord.Member = None):
    if user is None:
        user = ctx.message.author

    inline = True
    embed = nextcord.Embed(title=f"{user.name}#{user.discriminator}", color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
    userData = {
        "Mention": user.mention,
        "Nick": user.nick,
        "Created at": user.created_at.strftime("%b %d, %Y, %T"),
        "Joined at": user.joined_at.strftime("%b %d, %Y, %T"),
        "Server": user.guild,
        "Top Role": user.top_role
    }
    for [fieldName, fieldVal] in userData.items():
        embed.add_field(name=fieldName + ":", value=fieldVal, inline=inline)

    embed.set_thumbnail(user.display_avatar)
    await ctx.send(embed=embed)


@bot.command(aliases=["forecast"], description="Displays weather forecast for a chosen city")
async def weather(ctx: commands.Context, *, city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": city
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
            data = await res.json()

            location = data["location"]["name"]
            region = data["location"]["region"]
            country = data["location"]["country"]
            localtime = data["location"]["localtime"]
            temp_c = data["current"]["temp_c"]
            temp_f = data["current"]["temp_f"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]
            wind_mph = data["current"]["wind_mph"]
            condition = data["current"]["condition"]["text"]
            cloud = data["current"]["cloud"]
            pressure_mb = data["current"]["pressure_mb"]
            pressure_in = data["current"]["pressure_in"]
            image_url = "http:" + data["current"]["condition"]["icon"]

            embed = nextcord.Embed(title=f"Weather for {location}",
                                   description=f"The condition in ``{location}`` is ``{condition}``", color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="Region", value=f"{region}")
            embed.add_field(name="Country", value=f"{country}")
            embed.add_field(name="Local Time", value=f"{localtime}")
            embed.add_field(name="Temperature", value=f"C: {temp_c}  |  F: {temp_f}")
            embed.add_field(name="Humidity", value=f"{humidity}")
            embed.add_field(name="Wind Speeds", value=f"KPH: {wind_kph}  |  MPH: {wind_mph}")
            embed.add_field(name="Cloud", value=f"{cloud}")
            embed.add_field(name="Pressure", value=f"MB: {pressure_mb}  |  IN: {pressure_in}")
            embed.add_field(name="Source: ", value=f"https://weatherapi.com/")
            embed.set_thumbnail(url=image_url)
            embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def iplookup(ctx, *, ip):
    ip = ip
    api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
    info = response
    valid = info["is_valid"]
    country = info["country"]
    country_code = info["country_code"]
    region = info["region_code"]
    city = info["city"]
    zip = info["zip"]
    timezone = info["timezone"]
    isp = info["isp"]
    address = info["address"]

    embed = nextcord.Embed(title=f":mag: IP Lookup for {ip}",
                           description=f"Here's what I found about ``{ip}``",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="Valid:", value=f"{valid}")
    embed.add_field(name="Country:", value=f"{country}")
    embed.add_field(name="Country Code:", value=f"{country_code}")
    embed.add_field(name="Region:", value=f"{region}")
    embed.add_field(name="City:", value=f"{city}")
    embed.add_field(name="Zip:", value=f"{zip}")
    embed.add_field(name="Timezone:", value=f"{timezone}")
    embed.add_field(name="ISP:", value=f"{isp}")
    embed.add_field(name="Address:", value=f"{address}")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def urllookup(ctx, *, url):
    api_url = 'https://api.api-ninjas.com/v1/urllookup?url={}'.format(url)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
    info = response
    valid = info["is_valid"]
    country = info["country"]
    country_code = info["country_code"]
    region_code = info["region_code"]
    region = info["region"]
    city = info["city"]
    zip = info["zip"]
    lat = info["lat"]
    lon = info["lon"]
    timezone = info["timezone"]
    isp = info["isp"]
    url = info["url"]

    embed = nextcord.Embed(title=f":mag: URL Lookup for {url}",
                           description=f"Here's what I found about ``{url}``",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="Valid:", value=f"{valid}")
    embed.add_field(name="Country:", value=f"{country}")
    embed.add_field(name="Country Code:", value=f"{country_code}")
    embed.add_field(name="Region:", value=f"{region}")
    embed.add_field(name="Region Code:", value=f"{region_code}")
    embed.add_field(name="City:", value=f"{city}")
    embed.add_field(name="Zip:", value=f"{zip}")
    embed.add_field(name="Lat.:", value=f"{lat}")
    embed.add_field(name="Lon.:", value=f"{lon}")
    embed.add_field(name="Timezone:", value=f"{timezone}")
    embed.add_field(name="ISP:", value=f"{isp}")
    embed.add_field(name="URL:", value=f"https://{url}/")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command()
async def city(ctx, *, city):
    city = city
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
    info = response[0]
    name = info["name"]
    latitude = info["latitude"]
    longitude = info["longitude"]
    country = info["country"]
    population = info["population"]
    is_capital = info["is_capital"]

    embed = nextcord.Embed(title=f":earth_africa: Information about {name}",
                           description=f"Here's information about ``{name}``",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="Name:", value=f"{name}")
    embed.add_field(name="Latitude:", value=f"{latitude}")
    embed.add_field(name="Longitude:", value=f"{longitude}")
    embed.add_field(name="Country:", value=f"{country}")
    embed.add_field(name="Population:", value=f"{population}")
    embed.add_field(name="Capital:", value=f"{is_capital}")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command(aliases=["dict"])
async def dictionary(ctx, *, word):
    api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
    info = response
    word = info["word"]
    definition = info["definition"]
    valid = info["valid"]

    embed = nextcord.Embed(title=f":book: Here is the definition of {word}",
                           description=f"{definition}",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="Valid:", value=f"{valid}")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command(aliases=["date", "now", "calendar", "clock"])
async def time(ctx, *, city):
    api_url = 'https://api.api-ninjas.com/v1/worldtime?city={}'.format(city)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
    info = response
    timezone = info["timezone"]
    datentime = info["datetime"]
    day = info["day_of_week"]

    embed = nextcord.Embed(title=f":clock1: Current time in {city}",
                           description=f"",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="Timezone:", value=f"{timezone}")
    embed.add_field(name="Date & Time:", value=f"{datentime}")
    embed.add_field(name="Day of the week:", value=f"{day}")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command()
async def lorem(ctx, *, paragraphs: int):
    api_url = 'https://api.api-ninjas.com/v1/loremipsum?paragraphs={}'.format(paragraphs)
    response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
    info = response
    text = info["text"]

    if paragraphs <= 2:
        embed = nextcord.Embed(title=f":newspaper: Here's your lorem ipsum",
                               description=f"Paragraphs: {paragraphs}",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)
        await ctx.send(text)
    else:
        embed = nextcord.Embed(title=f":x: Paragraphs number cannot exceed 2.",
                               description=f"```{paragraphs}/2```", color=lunablue)
        embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)


@bot.command(aliases=["wikipedia"])
async def wiki(ctx, *, query):
    link = f"https://en.wikipedia.org/wiki/{query}"
    request = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}")
    page = request.json()
    description = page["extract"]
    title = page["title"]
    lang = page["lang"]

    embed = nextcord.Embed(title=f":newspaper: Here's what I found about {query}",
                           description=f"",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="Title:", value=f"{title}")
    embed.add_field(name="Language:", value=f"{lang}")
    embed.add_field(name="Description:", value=f"{description}")
    embed.add_field(name="Read whole article:", value=f"{link}")
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Wikipedia-logo-pt.svg/800px-Wikipedia-logo-pt.svg.png")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


@bot.command()
async def translate(ctx, l_from, l_to, *, query):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

    payload = {
        "from": f"{l_from}",
        "to": f"{l_to}",
        "q": f"{query}"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": f"{TRANSLATE_KEY}",
        "X-RapidAPI-Host": f"{TRANSLATE_HOST}"
    }

    response = requests.post(url, json=payload, headers=headers).json()
    data = response[0]

    embed = nextcord.Embed(title=f":page_facing_up: LUNA Translator",
                           description=f"",
                           color=lunaorange,
                           timestamp=ctx.message.created_at)
    embed.add_field(name="From:", value=f"{l_from}")
    embed.add_field(name="To:", value=f"{l_to}")
    embed.add_field(name="Query:", value=f"{query}")
    embed.add_field(name="Translation:", value=f"{data}")
    embed.set_footer(text=f"{bot.user.name} ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

    await ctx.send(embed=embed)


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


@bot.command()
async def trivia(ctx, *, category=None):
    if category is None:
        embed = nextcord.Embed(title=f":grey_question: Please choose a category",
                               description=f"Type .trivia [category] to start!",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.add_field(name="Categories:", value=f"`artliterature` `language`", inline=False)
        embed.add_field(name="", value=f"`sciencenature` `general`", inline=False)
        embed.add_field(name="", value=f"`fooddrink` `peopleplaces`", inline=False)
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


# -------------------------------------------------- Running the bot ---------------------------------------------------
bot.run(token)
