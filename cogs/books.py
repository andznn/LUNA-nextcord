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

    @commands.command()
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
                    subject_places = book_resp["subject_places"][0]
                    subjects = book_resp["subjects"][0]
                    subject_people = book_resp["subject_people"][0]
                    subject_times = book_resp["subject_times"][0]
                    created = book_resp["created"]["value"]
                    author_api = f"https://openlibrary.org/{author}.json"
                    author_resp = requests.get(author_api).json()
                    author_name = author_resp["name"]
                    cover_image = f"https://covers.openlibrary.org/b/id/{cover}-L.jpg"

                    embed = nextcord.Embed(title=f":book: {title}",
                                           description=f"Here's what I found about ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Title:", value=f"{title}")
                    embed.add_field(name="Author:", value=f"{author_name}")
                    embed.add_field(name="Created:", value=f"{created}")
                    embed.set_image(url=cover_image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    await ctx.send(embed=embed)

                except IndexError:
                    embed = nextcord.Embed(title=f":x: Didn't find anything related to {query}",
                                           description=f'Please try again!',
                                           color=lunablue, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(books(bot))
