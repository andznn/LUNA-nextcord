"""
This is a cog file of LUNA✱ Containing movies commands
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


class movies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def movie(self, ctx, *, title):
        try:
            async with ctx.typing():
                global genre_id
                url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=true&language=en-US&page=1"

                headers = {
                    "accept": "application/json",
                    "Authorization": f"{TMDB_KEY}"
                }

                response = requests.get(url, headers=headers).json()
                results = response["results"][0]

                id = results["id"]
                adult = results["adult"]
                original_language = results["original_language"]
                original_title = results["original_title"]
                overview = results["overview"]
                popularity = results["popularity"]
                release = results["release_date"]
                vote_average = results["vote_average"]
                vote_count = results["vote_count"]
                genres = results["genre_ids"]

                embed = nextcord.Embed(title=f":film_frames: {original_title}",
                                       description=f"Here's what I found about ``{title}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Title:", value=f"{original_title}")
                embed.add_field(name="Genres:", value=f"", inline=False)

                genre_url = "https://api.themoviedb.org/3/genre/movie/list"

                headers = {
                    "accept": "application/json",
                    "Authorization": f"{TMDB_KEY}"
                }
                genres_response = requests.get(genre_url, headers=headers).json()
                for (v) in genres:
                    for values in genres_response["genres"]:
                        if v == values["id"]:
                            embed.add_field(name="", value=f"`{values['name']}`", inline=True)
                        else:
                            pass

                info_url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

                headers = {
                    "accept": "application/json",
                    "Authorization": f"{TMDB_KEY}"
                }

                info_response = requests.get(info_url, headers=headers).json()

                budget = info_response["budget"]
                homepage = info_response["homepage"]
                background = info_response["poster_path"]
                revenue = info_response["revenue"]
                runtime = info_response["runtime"]
                tagline = info_response["tagline"]

                embed.add_field(name="Language:", value=f"{original_language}", inline=False)
                embed.add_field(name="Adult:", value=f"{adult}", inline=False)
                embed.add_field(name="Popularity:", value=f"{popularity}", inline=False)
                embed.add_field(name="Released:", value=f"{release}", inline=False)
                embed.add_field(name="Budget:", value=f"${budget}", inline=False)
                embed.add_field(name="Revenue:", value=f"${revenue}", inline=False)
                embed.add_field(name="Runtime:", value=f"{runtime}m", inline=False)
                embed.add_field(name="Vote Average:", value=f"{vote_average}")
                embed.add_field(name="Vote Count:", value=f"{vote_count}")
                embed.add_field(name="Tagline:", value=f"{tagline}", inline=False)
                embed.add_field(name="Description:", value=f"{overview[:600]}...", inline=False)
                embed.add_field(name="Homepage:", value=f"{homepage}", inline=False)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_image(url=f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2/{background}")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {title}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def series(self, ctx, *, title):
        try:
            async with ctx.typing():
                series_url = f"https://api.themoviedb.org/3/search/tv?query={title}&include_adult=true&language=en-US&page=1"

                headers = {
                    "accept": "application/json",
                    "Authorization": f"{TMDB_KEY}"
                }

                responseid = requests.get(series_url, headers=headers).json()
                results = responseid["results"][0]
                id = results["id"]

                url = f"https://api.themoviedb.org/3/tv/{id}?language=en-US"

                headers = {
                    "accept": "application/json",
                    "Authorization": f"{TMDB_KEY}"
                }

                response = requests.get(url, headers=headers).json()
                adult = response["adult"]
                creator = response["created_by"][0]
                creator_name = creator["name"]
                creator_gender = creator["gender"]
                first_episode = response["first_air_date"]
                genres = response["genres"]
                homepage = response["homepage"]
                in_production = response["in_production"]
                last_air_date = response["last_air_date"]
                original_title = response["name"]
                episodes = response["number_of_episodes"]
                seasons = response["number_of_seasons"]
                language = response["original_language"]
                overview = response["overview"]
                status = response["status"]
                tagline = response["tagline"]
                cover = response["poster_path"]

                embed = nextcord.Embed(title=f":film_frames: {original_title}",
                                       description=f"Here's what I found about ``{title}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Title:", value=f"{original_title}")
                embed.add_field(name="Genres:", value=f"", inline=False)
                for x in genres:
                    embed.add_field(name="", value=f"`{x['name']}`", inline=True)
                embed.add_field(name="Adult:", value=f"{adult}", inline=False)
                if creator_gender == 1:
                    embed.add_field(name="Creator:", value=f"{creator_name}", inline=False)
                    embed.add_field(name="", value=f"Gender: Female", inline=False)
                else:
                    embed.add_field(name="Creator:", value=f"{creator_name}", inline=False)
                    embed.add_field(name="", value=f"Gender: Male", inline=False)
                embed.add_field(name="First Episode Aired:", value=f"{first_episode}", inline=False)
                embed.add_field(name="Latest Episode Aired:", value=f"{last_air_date}", inline=False)
                embed.add_field(name="In Production:", value=f"{in_production}", inline=False)
                embed.add_field(name="Episodes:", value=f"{episodes}", inline=False)
                embed.add_field(name="Seasons:", value=f"{seasons}", inline=False)
                embed.add_field(name="Language:", value=f"{language}", inline=False)
                embed.add_field(name="Status:", value=f"{status}", inline=False)
                embed.add_field(name="Tagline:", value=f"{tagline}", inline=False)
                embed.add_field(name="Description:", value=f"{overview[:600]}...", inline=False)
                embed.add_field(name="Homepage:", value=f"{homepage}", inline=False)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_image(url=f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2/{cover}")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {title}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(movies(bot))
