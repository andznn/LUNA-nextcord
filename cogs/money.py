"""
This is a cog file of LUNA✱ Containing money commands
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


class money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["change", "pair"])
    async def exchange(self, ctx, *, pair):
        try:
            async with ctx.typing():
                pair = pair
                api_url = 'https://api.api-ninjas.com/v1/exchangerate?pair={}'.format(pair)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response
                currency_pair = info["currency_pair"]
                exchange_rate = info["exchange_rate"]

                embed = nextcord.Embed(title=f":chart: Exchange rates for {pair}",
                                       description=f"Here's current exchange for ``{pair}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Pair:", value=f"{currency_pair}")
                embed.add_field(name="Exchange:", value=f"{exchange_rate}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything about {pair}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def crypto(self, ctx, *, symbol):
        try:
            async with ctx.typing():
                symbol = symbol
                api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response
                name = info["symbol"]
                price = info["price"]

                embed = nextcord.Embed(title=f":coin: Current price of {symbol}",
                                       description=f"Here's current price of ``{symbol}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Symbol:", value=f"{name}")
                embed.add_field(name="Price:", value=f"{price}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything about {symbol}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def inflation(self, ctx, *, country):
        try:
            async with ctx.typing():
                api_url = 'https://api.api-ninjas.com/v1/inflation?country={}'.format(country)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                country = info["country"]
                type = info["type"]
                period = info["period"]
                monthly_rate_pct = info["monthly_rate_pct"]
                yearly_rate_pct = info["yearly_rate_pct"]

                embed = nextcord.Embed(title=f":chart_with_downwards_trend: Here's current inflation of {country}",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Country:", value=f"{country}")
                embed.add_field(name="Type:", value=f"{type}")
                embed.add_field(name="Period:", value=f"{period}")
                embed.add_field(name="Monthly:", value=f"{monthly_rate_pct}")
                embed.add_field(name="Yearly:", value=f"{yearly_rate_pct}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything about {country}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(money(bot))
