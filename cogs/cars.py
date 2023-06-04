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

class cars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def carporn(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('carporn')
                top_posts = subreddit.hot(limit=100)

                carporn = [post for post in top_posts if
                           not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not carporn:
                    await ctx.send('No cars found :(')
                    return

                random_car = random.choice(carporn)
                embed = nextcord.Embed(title=random_car.title, color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_car.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any images",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def jdm(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('JDM')
                top_posts = subreddit.hot(limit=100)

                JDM = [post for post in top_posts if
                           not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not JDM:
                    await ctx.send('No cars found :(')
                    return

                random_car = random.choice(JDM)
                embed = nextcord.Embed(title=random_car.title, color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_car.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any images",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["vin"])
    async def vinlookup(self, ctx, *, vin):
        try:
            async with ctx.typing():
                api_url = 'https://api.api-ninjas.com/v1/vinlookup?vin={}'.format(vin)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response
                vin = info["vin"]
                country = info["country"]
                manufacturer = info["manufacturer"]
                region = info["region"]
                wmi = info["wmi"]
                vds = info["vds"]
                vis = info["vis"]
                years = info["years"][0]

                embed = nextcord.Embed(title=f":mag: VIN Lookup for {vin}",
                                       description=f"Here's what I found about ``{vin}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="VIN:", value=f"{vin}")
                embed.add_field(name="Country:", value=f"{country}")
                embed.add_field(name="Manufacturer:", value=f"{manufacturer}")
                embed.add_field(name="Region:", value=f"{region}")
                embed.add_field(name="WMI:", value=f"{wmi}")
                embed.add_field(name="VDS:", value=f"{vds}")
                embed.add_field(name="VIS:", value=f"{vis}")
                embed.add_field(name="Years:", value=f"{years}+")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any info about {vin}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["carlookup", "cars", "vehicle"])
    async def car(self, ctx, *, model):
        try:
            async with ctx.typing():
                model = model
                api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                car_class = info["class"]
                cylinders = info["cylinders"]
                drive = info["drive"]
                fuel_type = info["fuel_type"]
                make = info["make"]
                model = info["model"]
                transmission = info["transmission"]
                year = info["year"]

                embed = nextcord.Embed(title=f":wheel: {model}",
                                       description=f"Here's what I found about ``{model}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Make:", value=f"{make}")
                embed.add_field(name="Model:", value=f"{model}")
                embed.add_field(name="Car Class:", value=f"{car_class}")
                embed.add_field(name="Cylinders:", value=f"{cylinders}...")
                embed.add_field(name="Drive:", value=f"{drive}")
                embed.add_field(name="Fuel:", value=f"{fuel_type}")
                embed.add_field(name="Transmission:", value=f"{transmission}")
                embed.add_field(name="Year:", value=f"{year}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any info about {model}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(cars(bot))
