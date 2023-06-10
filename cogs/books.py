"""
This is a cog file of LUNA✱ Containing books commands
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


class books(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["library", "lib", "bookshelf", "books"])
    async def book(self, ctx, action, *, query):
        async with ctx.typing():
            if action == "search":
                try:
                    api = f"https://openlibrary.org/search.json?q={query}"
                    response = requests.get(api).json()
                    docs = response["docs"][0]
                    key = docs["key"]
                    book_api = f"https://openlibrary.org/{key}.json"
                    book_resp = requests.get(book_api).json()
                    title = book_resp["title"]
                    author = book_resp["authors"][0]["author"]["key"]
                    description = book_resp["description"]
                    cover = book_resp["covers"][0]
                    try:
                        subject_places = book_resp["subject_places"]
                    except:
                        subject_places = "-"
                    try:
                        subjects = book_resp["subjects"]
                    except:
                        subjects = "-"
                    try:
                        subject_people = book_resp["subject_people"]
                    except:
                        subject_people = "-"
                    try:
                        subject_times = book_resp["subject_times"]
                    except:
                        subject_times = "-"
                    try:
                        created = book_resp["created"]["value"]
                    except:
                        created = "N/A"
                    author_api = f"https://openlibrary.org/{author}.json"
                    author_resp = requests.get(author_api).json()
                    author_name = author_resp["name"]
                    cover_image = f"https://covers.openlibrary.org/b/id/{cover}-L.jpg"

                    embed = nextcord.Embed(title=f":book: {title}",
                                           description=f"Here's what I found about ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Title:", value=f"{title}", inline=True)
                    embed.add_field(name="Author:", value=f"{author_name}", inline=True)
                    embed.add_field(name="Created:", value=f"{created}", inline=False)
                    embed.add_field(name="Subject Places:", value=f"", inline=False)
                    index = 0
                    limit = 5
                    for x in subject_places:
                        embed.add_field(name="", value=f"`{x}`", inline=True)
                        index += 1
                        if index == limit:
                            break
                    embed.add_field(name="Subjects:", value=f"", inline=False)
                    index = 0
                    limit = 5
                    for x in subjects:
                        embed.add_field(name="", value=f"`{x}`", inline=True)
                        index += 1
                        if index == limit:
                            break
                    embed.add_field(name="Subject People:", value=f"", inline=False)
                    index = 0
                    limit = 5
                    for x in subject_people:
                        embed.add_field(name="", value=f"`{x}`", inline=True)
                        index += 1
                        if index == limit:
                            break
                    embed.add_field(name="Subject Times:", value=f"", inline=False)
                    index = 0
                    limit = 5
                    for x in subject_times:
                        embed.add_field(name="", value=f"`{x}`", inline=True)
                        index += 1
                        if index == limit:
                            break
                    embed.add_field(name="Description:", value=f"{description[:1000]}...", inline=False)
                    embed.add_field(name="More information:", value=f"https://openlibrary.org{key}")
                    embed.set_image(url=cover_image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    await ctx.send(embed=embed)

                except IndexError:
                    embed = nextcord.Embed(title=f":x: Didn't find anything related to {query}",
                                           description=f'Please try again!',
                                           color=lunablue, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)

            if action == "author":
                try:
                    api = f"https://openlibrary.org/search/authors.json?q={query}"
                    response = requests.get(api).json()
                    docs = response["docs"][0]
                    key = docs["key"]
                    name = docs["name"]
                    try:
                        birth_date = docs["birth_date"]
                    except:
                        birth_date = "N/A"
                    try:
                        top_work = docs["top_work"]
                    except:
                        top_work = "N/A"
                    work_count = docs["work_count"]
                    top_subjects = docs["top_subjects"]
                    try:
                        other_names = docs["alternate_names"]
                    except:
                        other_names = "N/A"
                    image_api = f"https://covers.openlibrary.org/a/olid/{key}-L.jpg"

                    embed = nextcord.Embed(title=f":pen_ballpoint: {name}",
                                           description=f"Here's what I found about ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}", inline=False)
                    embed.add_field(name="Birth Date:", value=f"{birth_date}", inline=False)
                    embed.add_field(name="Top Work:", value=f"{top_work}", inline=False)
                    embed.add_field(name="Work Count:", value=f"{work_count}", inline=False)
                    embed.add_field(name="Top Subjects:", value=f"", inline=False)
                    index = 0
                    limit = 5
                    for x in top_subjects:
                        embed.add_field(name="", value=f"`{x}`", inline=True)
                        index += 1
                        if index == limit:
                            break
                    embed.add_field(name="Other Names:", value=f"", inline=False)
                    index = 0
                    limit = 5
                    for x in other_names:
                        embed.add_field(name="", value=f"`{x}`", inline=True)
                        index += 1
                        if index == limit:
                            break
                    embed.add_field(name="More Information:", value=f"https://openlibrary.org/authors/{key}",
                                    inline=False)
                    embed.set_image(url=image_api)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    await ctx.send(embed=embed)

                except IndexError:
                    embed = nextcord.Embed(title=f":x: Didn't find anything related to {query}",
                                           description=f'Please try again!',
                                           color=lunablue, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)

            else:
                embed = nextcord.Embed(title=f":x: Wrong action, use .book search/author [query]",
                                       description=f'Please try again!',
                                       color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(books(bot))
