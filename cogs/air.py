"""
This is a cog file of LUNA✱ Containing air commands
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


class air(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def airline(self, ctx, *, name):
        try:
            api = f"https://api.api-ninjas.com/v1/airlines?name={name}"
            response = requests.get(api, headers={"X-Api-Key": NINJAS_KEY}).json()
            info = response[0]
            fleet = info["fleet"]
            iata = info["iata"]
            icao = info["icao"]
            logo = info["logo_url"]
            name = info["name"]
            embed = nextcord.Embed(title=f":airplane: Airline Info",
                                   description=f"Here's information about `{name}`",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="Name:", value=f"{name}")
            embed.add_field(name="IATA:", value=f"{iata}")
            embed.add_field(name="ICAO:", value=f"{icao}")
            embed.add_field(name="Fleet:", value=f"")

            for (k, v) in fleet.items():
                embed.add_field(name=f"`{k}`", value=f"{v}")

            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            embed.set_image(url=logo)

            await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def airport(self, ctx, *, name):
        try:
            api = f"https://api.api-ninjas.com/v1/airports?name={name}"
            response = requests.get(api, headers={"X-Api-Key": NINJAS_KEY}).json()
            info = response[0]
            iata = info["iata"]
            icao = info["icao"]
            name = info["name"]
            city = info["city"]
            region = info["region"]
            country = info["country"]
            elevation = info["elevation_ft"]
            latitude = info["latitude"]
            longitude = info["longitude"]
            timezone = info["timezone"]

            embed = nextcord.Embed(title=f":airplane_arriving: Information about {name}",
                                   description=f"Here's information about ``{name}``",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="Name:", value=f"{name}")
            embed.add_field(name="IATA:", value=f"{iata}")
            embed.add_field(name="ICAO:", value=f"{icao}")
            embed.add_field(name="City:", value=f"{city}")
            embed.add_field(name="Region:", value=f"{region}")
            embed.add_field(name="Country:", value=f"{country}")
            embed.add_field(name="Elevation (ft):", value=f"{elevation}")
            embed.add_field(name="Latitude:", value=f"{latitude}")
            embed.add_field(name="Longitude:", value=f"{longitude}")
            embed.add_field(name="Timezone:", value=f"{timezone}")
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def air(self, ctx, *, city):
        try:
            api = f"https://api.api-ninjas.com/v1/airquality?city={city}"
            response = requests.get(api, headers={"X-Api-Key": NINJAS_KEY}).json()
            info = response
            name = city
            overall_aqi = info["overall_aqi"]
            coc = info["CO"]["concentration"]
            coo = info["CO"]["aqi"]
            pm10 = info["PM10"]["concentration"]
            pm10o = info["PM10"]["aqi"]
            so2 = info["SO2"]["concentration"]
            so2o = info["SO2"]["aqi"]
            pm2 = info["PM2.5"]["concentration"]
            pm2o = info["PM2.5"]["aqi"]
            o3 = info["O3"]["concentration"]
            o3o = info["O3"]["aqi"]
            no2 = info["NO2"]["concentration"]
            no2o = info["NO2"]["aqi"]

            embed = nextcord.Embed(title=f":airplane_arriving: Information about {name}",
                                   description=f"Here's information about ``{name}``",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="Name:", value=f"{name}")
            embed.add_field(name="Overall Quality:", value=f"`{overall_aqi}`")
            embed.add_field(name="CO:", value=f"Concentration: `{coc}` | AQI: `{coo}`", inline=False)
            embed.add_field(name="PM10:", value=f"Concentration: `{pm10}` | AQI: `{pm10o}`", inline=False)
            embed.add_field(name="SO2:", value=f"Concentration: `{so2}` | AQI: `{so2o}`", inline=False)
            embed.add_field(name="PM2.5:", value=f"Concentration: `{pm2}` | AQI: `{pm2o}`", inline=False)
            embed.add_field(name="O3:", value=f"Concentration: `{o3}` | AQI: `{o3o}`", inline=False)
            embed.add_field(name="NO2:", value=f"Concentration: `{no2}` | AQI: `{no2o}`", inline=False)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(air(bot))
