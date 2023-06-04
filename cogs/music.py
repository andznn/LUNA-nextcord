"""
This is a cog file of LUNA✱ Containing music search commands
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


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def music(self, ctx, type, *, query):
        try:
            async with ctx.typing():
                if type == "artist":
                    url = "https://genius-song-lyrics1.p.rapidapi.com/search/multi/"

                    querystring = {"q": f"{query}", "per_page": "3", "page": "1"}

                    headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }

                    response = requests.get(url, headers=headers, params=querystring).json()
                    info = response
                    name = info["sections"][3]["hits"][0]["result"]["name"]
                    image = info["sections"][3]["hits"][0]["result"]["header_image_url"]
                    genius_profile = info["sections"][3]["hits"][0]["result"]["url"]
                    best_song = info["sections"][1]["hits"][0]["result"]["title"]
                    best_song_lyrics = info["sections"][1]["hits"][0]["result"]["url"]
                    id = info["sections"][3]["hits"][0]["result"]["id"]

                    artist_url = "https://genius-song-lyrics1.p.rapidapi.com/artist/details/"

                    artist_querystring = {"id": f"{id}"}
                    artist_headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }
                    artist_response = requests.get(artist_url, headers=artist_headers, params=artist_querystring).json()
                    artist_data = artist_response
                    description = artist_data["artist"]["description_preview"]
                    genius_followers = artist_data["artist"]["followers_count"]
                    facebook = artist_data["artist"]["facebook_name"]
                    instagram = artist_data["artist"]["instagram_name"]

                    embed = nextcord.Embed(title=f":cd: {query}", description=f"Here's what I found about ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}", inline=False)
                    embed.add_field(name="Genius Followers:", value=f"{genius_followers}", inline=False)
                    embed.add_field(name="Facebook:", value=f"{facebook}", inline=False)
                    embed.add_field(name="Instagram:", value=f"{instagram}", inline=False)
                    embed.add_field(name="Genius Profile:", value=f"{genius_profile}", inline=False)
                    embed.add_field(name="Most Popular Song:", value=f"{best_song}", inline=False)
                    embed.add_field(name="Song Lyrics Link:", value=f"{best_song_lyrics}", inline=False)
                    embed.add_field(name="Description:", value=f"{description[:500]}...", inline=False)
                    embed.set_image(url=image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)

                if type == "album":
                    url = "https://genius-song-lyrics1.p.rapidapi.com/search/multi/"

                    querystring = {"q": f"{query}", "per_page": "3", "page": "1"}

                    headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }

                    response = requests.get(url, headers=headers, params=querystring).json()
                    info = response
                    name = info["sections"][4]["hits"][0]["result"]["name"]
                    image = info["sections"][4]["hits"][0]["result"]["cover_art_url"]
                    album_url = info["sections"][4]["hits"][0]["result"]["url"]
                    artist = info["sections"][4]["hits"][0]["result"]["artist"]["name"]
                    artist_url = info["sections"][4]["hits"][0]["result"]["artist"]["url"]
                    release = info["sections"][4]["hits"][0]["result"]["release_date_for_display"]
                    id = info["sections"][4]["hits"][0]["result"]["id"]

                    album_url = "https://genius-song-lyrics1.p.rapidapi.com/album/details/"

                    album_querystring = {"id": f"{id}"}
                    album_headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }
                    album_response = requests.get(album_url, headers=album_headers, params=album_querystring).json()
                    album_data = album_response
                    description = album_data["album"]["description_preview"]
                    artist_image = album_data["album"]["artist"]["image_url"]

                    embed = nextcord.Embed(title=f":cd: {query}", description=f"Here's what I found about ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}", inline=False)
                    embed.add_field(name="Album Link:", value=f"{album_url}", inline=False)
                    embed.add_field(name="Artist:", value=f"{artist}", inline=False)
                    embed.add_field(name="Artist Link:", value=f"{artist_url}", inline=False)
                    embed.add_field(name="Released:", value=f"{release}", inline=False)
                    embed.add_field(name="Description:", value=f"{description[:500]}", inline=False)
                    embed.set_image(url=image)
                    embed.set_thumbnail(url=artist_image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)

                if type == "song":
                    url = "https://genius-song-lyrics1.p.rapidapi.com/search/multi/"

                    querystring = {"q": f"{query}", "per_page": "3", "page": "1"}

                    headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }

                    response = requests.get(url, headers=headers, params=querystring).json()
                    info = response
                    name = info["sections"][2]["hits"][0]["result"]["title"]
                    image = info["sections"][2]["hits"][0]["result"]["song_art_image_url"]
                    artist = info["sections"][2]["hits"][0]["result"]["artist_names"]
                    language = info["sections"][2]["hits"][0]["result"]["language"]
                    lyrics_url = info["sections"][2]["hits"][0]["result"]["url"]
                    release = info["sections"][2]["hits"][0]["result"]["release_date_for_display"]
                    id = info["sections"][2]["hits"][0]["result"]["id"]

                    song_url = "https://genius-song-lyrics1.p.rapidapi.com/song/details/"

                    song_querystring = {"id": f"{id}"}
                    song_headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }
                    song_response = requests.get(song_url, headers=song_headers, params=song_querystring).json()
                    song_data = song_response
                    album = song_data["song"]["album"]["name"]
                    artist_image = song_data["song"]["album"]["artist"]["image_url"]
                    youtube = song_data["song"]["youtube_url"]

                    embed = nextcord.Embed(title=f":cd: {query}", description=f"Here's what I found about ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}", inline=False)
                    embed.add_field(name="Artist:", value=f"{artist}", inline=False)
                    embed.add_field(name="Language:", value=f"{language}", inline=False)
                    embed.add_field(name="Lyrics:", value=f"{lyrics_url}", inline=False)
                    embed.add_field(name="Released:", value=f"{release}", inline=False)
                    embed.add_field(name="Album:", value=f"{album}", inline=False)
                    embed.add_field(name="Youtube Link:", value=f"{youtube}", inline=False)
                    embed.set_image(url=image)
                    embed.set_thumbnail(url=artist_image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)

                if type == "lyrics":
                    url = "https://genius-song-lyrics1.p.rapidapi.com/search/multi/"

                    querystring = {"q": f"{query}", "per_page": "3", "page": "1"}

                    headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }

                    response = requests.get(url, headers=headers, params=querystring).json()
                    info = response
                    id = info["sections"][2]["hits"][0]["result"]["id"]
                    name = info["sections"][2]["hits"][0]["result"]["title"]
                    image = info["sections"][2]["hits"][0]["result"]["song_art_image_url"]
                    artist = info["sections"][2]["hits"][0]["result"]["artist_names"]

                    lyrics_url = "https://genius-song-lyrics1.p.rapidapi.com/song/lyrics/"

                    lyrics_querystring = {"id": f"{id}"}
                    lyrics_headers = {
                        "X-RapidAPI-Key": f"{GENIUS_KEY}",
                        "X-RapidAPI-Host": f"{GENIUS_HOST}"
                    }
                    lyrics_response = requests.get(lyrics_url, headers=lyrics_headers, params=lyrics_querystring).json()
                    lyrics_data = lyrics_response
                    lyrics_link = "https://genius.com" + lyrics_data["lyrics"]["path"]

                    embed = nextcord.Embed(title=f":cd: {query}", description=f"Here are the lyrics for ``{query}``",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}", inline=False)
                    embed.add_field(name="Artist:", value=f"{artist}", inline=False)
                    embed.add_field(name="Lyrics:", value=f"{lyrics_link}", inline=False)
                    embed.set_image(url=image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                    await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {query}", description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(music(bot))
