"""
This is a cog file of LUNA✱ Containing anime commands
"""
import nextcord
from nextcord.ext import commands
from config.colors import *
import AnilistPython
from AnilistPython import Anilist
from config.config import *


class anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Displays information about chosen anime title")
    async def anime(self, ctx, *, name):
        try:
            async with ctx.typing():
                anime = anilist.get_anime(name)
                name_r = anime["name_romaji"]
                name_e = anime["name_english"]
                airing_start = anime["starting_time"]
                airing_end = anime["ending_time"]
                aformat = anime["airing_format"]
                episodes = anime["airing_episodes"]
                season = anime["season"]
                description = anime["desc"]
                score = anime["average_score"]
                cover = anime["cover_image"]
                watchtime = episodes * 22
                watchtimeh = watchtime / 60
                watchtimeh = int(watchtimeh)
                genres = anime["genres"]

                embed = nextcord.Embed(title=f":film_frames: {name_r}", description=f"Here's what I found about ``{name}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Name Romaji:", value=f"{name_r}")
                embed.add_field(name="Name English:", value=f"{name_e}")
                embed.add_field(name="Airing Start:", value=f"{airing_start}")
                embed.add_field(name="Airing End:", value=f"{airing_end}")
                embed.add_field(name="Format:", value=f"{aformat}")
                embed.add_field(name="Episodes:", value=f"{episodes}")
                embed.add_field(name="Season:", value=f"{season}")
                embed.add_field(name="Score:", value=f"{score}")
                embed.add_field(name="Approx. Length:", value=f"{watchtimeh + 1}h")
                embed.add_field(name="Genres:", value=f"{genres}")
                embed.add_field(name="Description:", value=f"{description[:600]}...")
                embed.add_field(name="Source:", value="https://anilist.co")
                embed.set_image(url=cover)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description="Displays information about chosen manga title")
    async def manga(self, ctx, *, name):
        try:
            async with ctx.typing():
                manga = anilist.get_manga(name)
                name_r = manga["name_romaji"]
                name_e = manga["name_english"]
                airing_start = manga["starting_time"]
                airing_end = manga["ending_time"]
                aformat = manga["release_format"]
                chapters = manga["chapters"]
                volumes = manga["volumes"]
                description = manga["desc"]
                score = manga["mean_score"]
                cover = manga["cover_image"]
                genres = manga["genres"]

                embed = nextcord.Embed(title=f":book: {name_r}", description=f"Here's what I found about ``{name}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Name Romaji:", value=f"{name_r}")
                embed.add_field(name="Name English:", value=f"{name_e}")
                embed.add_field(name="Release Start:", value=f"{airing_start}")
                embed.add_field(name="Release End:", value=f"{airing_end}")
                embed.add_field(name="Format:", value=f"{aformat}")
                embed.add_field(name="Chapters:", value=f"{chapters}")
                embed.add_field(name="Volumes:", value=f"{volumes}")
                embed.add_field(name="Score:", value=f"{score}")
                embed.add_field(name="Genres:", value=f"{genres}")
                embed.add_field(name="Description:", value=f"{description[:600]}...")
                embed.add_field(name="Source:", value="https://anilist.co")
                embed.set_image(url=cover)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description="Displays information about chosen anime character")
    async def character(self, ctx, *, name):
        try:
            async with ctx.typing():
                char = anilist.get_character(name)
                firstname = char["first_name"]
                lastname = char["last_name"]
                native = char["native_name"]
                description = char["desc"]
                image = char["image"]

                embed = nextcord.Embed(title=f":person_bowing: {firstname}",
                                       description=f"Here's what I found about ``{name}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="First Name:", value=f"{firstname}")
                embed.add_field(name="Last Name:", value=f"{lastname}")
                embed.add_field(name="Native Name:", value=f"{native}")
                embed.add_field(name="Description:", value=f"{description[:600]}...")
                embed.add_field(name="Source:", value="https://anilist.co")
                embed.set_image(url=image)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def animelist(self, ctx, type, *, query):
        if type == "anilist":
            async with ctx.typing():
                embed = nextcord.Embed(title=f":newspaper: Here's {query}'s AniList",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Link:", value=f"https://anilist.co/user/{query}/animelist")
                embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/AniList_logo.svg/2048px-AniList_logo.svg.png")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        if type == "myanimelist":
            async with ctx.typing():
                embed = nextcord.Embed(title=f":newspaper: Here's {query}'s MyAnimeList",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Link:", value=f"https://myanimelist.net/profile/{query}")
                embed.set_image(
                    url="https://upload.wikimedia.org/wikipedia/commons/5/58/MyAnimeList_-_Full_Text_Logo.jpg")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(title=f":x: Bad arguments.",
                                   description=f"Use .animelist anilist/myanimelist [name]",
                                   color=lunablue)
            embed.set_footer(text=f"LUNA✱✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(anime(bot))
