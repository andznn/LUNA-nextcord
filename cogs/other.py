"""
This is a cog file of LUNA✱ Containing other and utility commands
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
import gtts
from gtts import gTTS
import logging
import pkg_resources


class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def imports(self, ctx):
        memberid = ctx.author.id
        if memberid == 782956226500755466:
            installed_packages = pkg_resources.working_set
            installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                              for i in installed_packages])
            embed = nextcord.Embed(title=f':package: Here are all the packages I am currently using...',
                                   description="", timestamp=ctx.message.created_at,
                                   color=lunablue)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            for v in installed_packages_list:
                embed.add_field(name=f"`{v}`", value="", inline=True)
            await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(title=f'Only my creator can use this command.',
                                   description=f'{ctx.author} Why are you even trying...',
                                   timestamp=ctx.message.created_at,
                                   color=lunablue)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

    @commands.command(aliases=['logoff', 'terminate'], hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
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
            await self.bot.close()
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

    @commands.command(description="Disables selected command")
    @commands.has_permissions(administrator=True)
    async def toggle(self, ctx, *, command):
        try:
            command = self.bot.get_command(command)
            if ctx.command == command:
                embed = nextcord.Embed(title=f':x: You cannot disable this command.', color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            else:
                command.enabled = not command.enabled
                ternary = "enabled" if command.enabled else "disabled"
                embed = nextcord.Embed(title=f':ballot_box_with_check: I {ternary} {command.qualified_name}',
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
        except AttributeError:
            embed = nextcord.Embed(title=f":x: Couldn't find that command",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["statistics", "uptime"])
    @commands.has_permissions(administrator=True)
    async def stats(self, ctx):
        global us, um, uh, ud
        embed = nextcord.Embed(title='My Stats', description='Uptime:', timestamp=ctx.message.created_at,
                               color=lunaorange)
        embed.add_field(name=f"Days: ", value=ud, inline=False)
        embed.add_field(name=f"Hours: ", value=uh, inline=False)
        embed.add_field(name=f"Minutes: ", value=um, inline=False)
        embed.add_field(name=f"Seconds: ", value=us, inline=False)
        embed.add_field(name=f"Name: ", value=f"LUNA✱")
        embed.add_field(name=f"Creator: ", value=f"{creator}")
        embed.add_field(name=f"Version: ", value=f"{version}")
        embed.add_field(name=f"Nextcord: ", value=f"{nextcordv}")
        embed.add_field(name=f"Python: ", value=f"{pythonv}")
        embed.add_field(name=f"Help Panel: ", value=f"Use .help")
        embed.add_field(name=f"Based on Nextcord", value=f"https://docs.nextcord.dev/en/stable/", inline=False)
        embed.add_field(name=f"GitHub Repository", value=f"https://github.com/andzn986/LUNA-nextcord/", inline=False)
        embed.set_image(url="https://i.ibb.co/jrNLFw2/lunatrans.png")
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=["inv"])
    @commands.has_permissions(create_instant_invite=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def invite(self, ctx):
        invite = await ctx.guild.text_channels[0].create_invite(max_age=0, max_uses=0)
        embed = nextcord.Embed(title=f":envelope_with_arrow: Success!",
                               description=f"Here's your invite {ctx.author.mention}", color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)
        await ctx.send(invite)

    @commands.command(aliases=['lvl', 'exp'], description="Displays users level")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def level(self, ctx, member: nextcord.Member = None):
        try:
            if not member:
                with open('users.json', 'r') as f:
                    users = json.load(f)
                lvl = users[str(ctx.message.author.id)]['level']
                embed = nextcord.Embed(title=f':bust_in_silhouette: You are at level {lvl}!', color=lunablue,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            if member.id == 1108328414823317504:
                embed = nextcord.Embed(title=f"I don't have a level!", color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            else:
                id = member.id
                with open('users.json', 'r') as f:
                    users = json.load(f)
                lvl = users[str(id)]['level']
                embed = nextcord.Embed(title=f':bust_in_silhouette: {member} is at level {lvl}!', color=lunablue,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
        except AttributeError:
            pass

    @commands.command(aliases=['remind', 'reminder', 'tr'], description="Sets a timer with a reminder")
    async def timer(self, ctx, seconds, *, reminder):
        try:
            secondint = int(seconds)
            if secondint > 300:
                embed = nextcord.Embed(title=f":x: Can't go over 5 minutes.", color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                raise BaseException
            if secondint <= 0:
                embed = nextcord.Embed(title=f":x: Number cannot be negative.", color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
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
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(f"{ctx.author.mention}", embed=embed)
        except ValueError:
            embed = nextcord.Embed(title=f":x: Missing argument. You must enter a number.", color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

    @commands.command(aliases=["version", "v"], description="Displays current bot version")
    async def ver(self, ctx):
        embed = nextcord.Embed(title=f":globe_with_meridians: LUNA✱",
                               description=f"```Version: {version}, Created by: {creator}```", color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.add_field(name='Nextcord Version:', value=nextcordv, inline=False)
        embed.add_field(name='Python Version:', value=pythonv, inline=False)
        embed.add_field(name='Read more about nextcord:', value="https://docs.nextcord.dev/en/stable/", inline=False)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["repeat"], description="Repeats users message")
    @commands.has_permissions(send_messages=True)
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(f"{text}")

    @commands.command(aliases=["shout"], description="Announces users message with @ everyone tag")
    @commands.has_permissions(mention_everyone=True)
    async def announce(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(f"@everyone")
        embed = nextcord.Embed(title=f":mega: {text}", description=f"Announcement by {ctx.author.mention}",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["latency"], description="Displays bot latency")
    async def ping(self, ctx):
        latency = self.bot.latency
        embed = nextcord.Embed(
            title=":inbox_tray: Pong! Here's my latency:",
            description=f'**{latency * 1000:.2f}ms**',
            color=lunaorange
        )
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=["pic", "pfp"], description="Sends users avatar")
    async def avatar(self, ctx, *, member: nextcord.Member = None):
        if member == None:
            member = ctx.author

        memberAvatar = member.avatar.url

        embed = nextcord.Embed(title=f"{member}'s avatar:", description=f"{member.mention}", color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_image(url=memberAvatar)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["si", "info", "server"], description="Displays current server info")
    async def serverinfo(self, ctx):
        global bot
        role_count = len(ctx.guild.roles)
        list_of_bots = [self.bot.mention for self.bot in ctx.guild.members if self.bot.bot]

        embed = nextcord.Embed(title=f':information_source: Server Info: {ctx.guild.name}',
                               timestamp=ctx.message.created_at,
                               color=lunaorange)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
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

    @commands.command()
    async def profile(self, ctx, user: nextcord.Member = None):
        if user is None:
            user = ctx.message.author

        inline = True
        embed = nextcord.Embed(title=f"{user.name}#{user.discriminator}", color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
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

    @commands.command(aliases=["forecast"], description="Displays weather forecast for a chosen city")
    async def weather(self, ctx: commands.Context, *, city):
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
                                       description=f"The condition in ``{location}`` is ``{condition}``",
                                       color=lunaorange,
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
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def iplookup(self, ctx, *, ip):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def urllookup(self, ctx, *, url):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def city(self, ctx, *, city):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["dict"])
    async def dictionary(self, ctx, *, word):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["date", "now", "calendar", "clock"])
    async def time(self, ctx, *, city):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def lorem(self, ctx, *, paragraphs: int):
        api_url = 'https://api.api-ninjas.com/v1/loremipsum?paragraphs={}'.format(paragraphs)
        response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
        info = response
        text = info["text"]

        if paragraphs <= 2:
            embed = nextcord.Embed(title=f":newspaper: Here's your lorem ipsum",
                                   description=f"Paragraphs: {paragraphs}",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)
            await ctx.send(text)
        else:
            embed = nextcord.Embed(title=f":x: Paragraphs number cannot exceed 2.",
                                   description=f"```{paragraphs}/2```", color=lunablue)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

    @commands.command(aliases=["wikipedia"])
    async def wiki(self, ctx, *, query):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def translate(self, ctx, l_from, l_to, *, query):
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
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(other(bot))
