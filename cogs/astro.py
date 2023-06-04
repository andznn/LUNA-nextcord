"""
This is a cog file of LUNA✱ Containing astro commands
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


class astro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def planet(self, ctx, *, planet):
        try:
            async with ctx.typing():
                query = planet
                api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(query)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]

                name = info["name"]
                mass = info["mass"]
                radius = info["radius"]
                period = info["period"]
                semi_major_axis = info["semi_major_axis"]
                temperature = info["temperature"]
                distance_light_year = info["distance_light_year"]
                host_star_mass = info["host_star_mass"]
                host_star_temperature = info["host_star_temperature"]

                embed = nextcord.Embed(title=f":ringed_planet: Here's information about {planet}", description='',
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.add_field(name="Name:", value=f"{name}")
                embed.add_field(name="Mass:", value=f"{mass}")
                embed.add_field(name="Radius:", value=f"{radius}")
                embed.add_field(name="Period:", value=f"{period}")
                embed.add_field(name="Semi Major Axis:", value=f"{semi_major_axis}")
                embed.add_field(name="Temperature:", value=f"{temperature}")
                embed.add_field(name="Distance Light Year:", value=f"{distance_light_year}")
                embed.add_field(name="Host Star Mass:", value=f"{host_star_mass}")
                embed.add_field(name="Host Star Temperature:", value=f"{host_star_temperature}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any info about {planet}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["APOD", "apod"])
    async def astrophoto(self, ctx):
        try:
            async with ctx.typing():
                api_url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}'
                response = requests.get(api_url).json()
                info = response

                date = info["date"]
                explanation = info["explanation"]
                title = info["title"]
                image = info["url"]

                embed = nextcord.Embed(title=f":camera: Here's astronomy picture of the day", description=f'{title}',
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.add_field(name="Date:", value=f"{date}")
                embed.add_field(name="Explanation:", value=f"{explanation[:350]}...")
                embed.set_image(url=image)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any image",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def horoscope(self, ctx, sign, period):
        try:
            async with ctx.typing():
                url = f"https://horoscopes-ai.p.rapidapi.com/get_horoscope_en/{sign}/{period}/general"
                headers = {
                    "X-RapidAPI-Key": f'{HOROSCOPE_KEY}',
                    "X-RapidAPI-Host": f'{HOROSCOPE_HOST}'
                }
                response = requests.get(url, headers=headers).json()
                info = response
                sign = info["sign"]
                period = info["period"]
                general = info["general"][0]

                embed = nextcord.Embed(title=f":{sign}: Here's horoscope for {sign} for {period}", description='',
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.add_field(name="Sign:", value=f"{sign}")
                embed.add_field(name="Period:", value=f"{period}")
                embed.add_field(name="Description:", value=f"{general}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except json.decoder.JSONDecodeError:
            embed = nextcord.Embed(title=f":x: Wrong arguments used! Use .help to see usage info", description=f'',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(astro(bot))
