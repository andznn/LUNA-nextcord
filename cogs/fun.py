"""
This is a cog file of LUNA✱ Containing fun commands
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
import gtts
from gtts import gTTS


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ai"], description='Prompts a message to ChatGPT')
    async def gpt(self, ctx: commands.Context, *, prompt: str):
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.5,
                "max_tokens": 50,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "best_of": 1,
            }
            headers = {"Authorization": f"Bearer {GPT}"}
            async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
                response = await resp.json()
                embed = nextcord.Embed(title="Chat GPT's Response:", description=response, color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)

    @commands.command(aliases=["memes", "memer"])
    async def meme(self, ctx, *, category=None):
        if category is None:
            subreddit = reddit.subreddit('memes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'categories':
            embed = nextcord.Embed(title="Available meme categories:", color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.add_field(name="``anime``", value="", inline=True)
            embed.add_field(name="``gamers``", value="", inline=True)
            embed.add_field(name="``cars``", value="", inline=True)
            embed.add_field(name="``gym``", value="", inline=True)
            embed.add_field(name="``dirty``", value="", inline=True)
            embed.add_field(name="``dank``", value="", inline=True)
            embed.add_field(name="``league``", value="", inline=True)
            embed.add_field(name="``rocket league``", value="", inline=True)
            embed.add_field(name="``minecraft``", value="", inline=True)
            embed.add_field(name="``csgo``", value="", inline=True)
            embed.add_field(name="``animals``", value="", inline=True)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'anime':
            subreddit = reddit.subreddit('animemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'gamers':
            subreddit = reddit.subreddit('animemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'cars':
            subreddit = reddit.subreddit('carmemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'gym':
            subreddit = reddit.subreddit('gymmemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'dirty':
            subreddit = reddit.subreddit('dirtymemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'dank':
            subreddit = reddit.subreddit('dankmemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == 'league':
            subreddit = reddit.subreddit('LeagueOfMemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == "rocket league":
            subreddit = reddit.subreddit('RocketLeagueMemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == "minecraft":
            subreddit = reddit.subreddit('MinecraftMemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == "csgo":
            subreddit = reddit.subreddit('CSGOmemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

        if category == "animals":
            subreddit = reddit.subreddit('AnimalMemes')
            top_posts = subreddit.hot(limit=100)

            memes = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not memes:
                await ctx.send('No memes found :(')
                return

            random_meme = random.choice(memes)
            embed = nextcord.Embed(title=random_meme.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_meme.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description='Sends a random spicy picture from r/passionx')
    @commands.is_nsfw()
    async def porn(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('passionx')
                top_posts = subreddit.hot(limit=100)

                porn = [post for post in top_posts if
                        not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not porn:
                    await ctx.send('No porn found :(')
                    return

                random_porn = random.choice(porn)
                embed = nextcord.Embed(title=random_porn.title, description="Via https://www.reddit.com/r/passionx/", color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_porn.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any porn",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description='Sends a random spicy picture from r/JustHentaiForYou')
    @commands.is_nsfw()
    async def hentai(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('JustHentaiForYou')
                top_posts = subreddit.hot(limit=100)

                hentai = [post for post in top_posts if
                          not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not hentai:
                    await ctx.send('No hentai found :(')
                    return

                random_hentai = random.choice(hentai)
                embed = nextcord.Embed(title=random_hentai.title, description="Via https://www.reddit.com/r/JustHentaiForYou/", color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_hentai.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any hentai",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description='Sends a random spicy picture from r/JustHentaiForYou')
    @commands.is_nsfw()
    async def feet(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('VerifiedFeet')
                top_posts = subreddit.hot(limit=100)

                feet = [post for post in top_posts if
                          not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not feet:
                    await ctx.send('No feet found :(')
                    return

                random_feet = random.choice(feet)
                embed = nextcord.Embed(title=random_feet.title, description="Via https://www.reddit.com/r/VerifiedFeet/", color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_feet.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any hentai",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description='Sends a random spicy picture from r/JustHentaiForYou')
    @commands.is_nsfw()
    async def cosplay(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('cosplay_babes')
                top_posts = subreddit.hot(limit=100)

                cosplay = [post for post in top_posts if
                          not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not cosplay:
                    await ctx.send('No feet found :(')
                    return

                random_cosp = random.choice(cosplay)
                embed = nextcord.Embed(title=random_cosp.title, description="Via https://www.reddit.com/r/cosplay_babes/", color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_cosp.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any hentai",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description='Sends a random spicy picture from r/Ecchi_Waifus')
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('Ecchi_Waifus')
                top_posts = subreddit.hot(limit=100)

                ecchi = [post for post in top_posts if
                         not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not ecchi:
                    await ctx.send('No ecchi found :(')
                    return

                random_ecchi = random.choice(ecchi)
                embed = nextcord.Embed(title=random_ecchi.title, description="Via https://www.reddit.com/r/Ecchi_Waifus/", color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_ecchi.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any ecchi",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(description='Sends a random spicy picture from r/Cursed')
    async def cursed(self, ctx):
        try:
            async with ctx.typing():
                subreddit = reddit.subreddit('Cursed')
                top_posts = subreddit.hot(limit=100)

                Cursed = [post for post in top_posts if
                          not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not Cursed:
                    await ctx.send('No ecchi found :(')
                    return

                random_Cursed = random.choice(Cursed)
                embed = nextcord.Embed(title=random_Cursed.title, color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_image(url=random_Cursed.url)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any cursed images",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def logo(self, ctx, *, company):
        try:
            async with ctx.typing():
                company = company
                api_url = 'https://api.api-ninjas.com/v1/logo?name={}'.format(company)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                name = info["name"]
                ticker = info["ticker"]
                image = info["image"]

                embed = nextcord.Embed(title=f"Logo look up for {company}",
                                       description=f"Here's what I found about ``{company}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Name:", value=f"{name}")
                embed.add_field(name="Ticker:", value=f"{ticker}")
                embed.set_image(url=image)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {company}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def emoji(self, ctx, *, name):
        try:
            async with ctx.typing():
                name = name
                api_url = 'https://api.api-ninjas.com/v1/emoji?name={}'.format(name)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                code = info["code"]
                character = info["character"]
                image = info["image"]
                name = info["name"]
                group = info["group"]
                subgroup = info["subgroup"]

                embed = nextcord.Embed(title=f":smile: Emoji Look Up for {name}",
                                       description=f"Here's what I found about ``{name}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Code:", value=f"{code}")
                embed.add_field(name="Character:", value=f"{character}")
                embed.add_field(name="Name:", value=f"{name}")
                embed.add_field(name="Group:", value=f"{group}")
                embed.add_field(name="Subgroup:", value=f"{subgroup}")
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
    async def quote(self, ctx, *, query):
        try:
            async with ctx.typing():
                query = query
                api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(query)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                quote = info["quote"]
                author = info["author"]
                category = info["category"]

                embed = nextcord.Embed(title=f":speech_left: Random quote about {query}",
                                       description=f"Here's a random quote about ``{query}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Quote:", value=f"{quote}")
                embed.add_field(name="Author:", value=f"{author}")
                embed.add_field(name="Category:", value=f"{category}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {query}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["celeb"])
    async def celebrity(self, ctx, *, name):
        try:
            async with ctx.typing():
                name = name
                api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                name = info["name"]
                net = info["net_worth"]
                gender = info["gender"]
                nationality = info["nationality"]
                occupation = info["occupation"][0]
                height = info["height"]
                birthday = info["birthday"]

                embed = nextcord.Embed(title=f":busts_in_silhouette: Information about {name}",
                                       description=f"Here's information about ``{name}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Name:", value=f"{name}")
                embed.add_field(name="Net worth:", value=f"{net}")
                embed.add_field(name="Gender:", value=f"{gender}")
                embed.add_field(name="Nationality:", value=f"{nationality}")
                embed.add_field(name="Occupation:", value=f"{occupation}")
                embed.add_field(name="Height:", value=f"{height}")
                embed.add_field(name="Birthday:", value=f"{birthday}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything related to {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def dadjoke(self, ctx):
        try:
            async with ctx.typing():
                api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(1)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                joke = info["joke"]

                embed = nextcord.Embed(title=f":rofl: Here's a dad joke",
                                       description=f"``{joke}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any jokes",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        try:
            async with ctx.typing():
                api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(1)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                joke = info["joke"]

                embed = nextcord.Embed(title=f":rofl: Here's a joke",
                                       description=f"``{joke}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any jokes",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def yesorno(self, ctx):
        try:
            async with ctx.typing():
                api_url = 'https://yesno.wtf/api'
                response = requests.get(api_url).json()
                info = response
                answer = info["answer"]
                image = info["image"]

                embed = nextcord.Embed(title=f"{answer}",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_image(url=image)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: API Error",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def flag(self, ctx, *, country):
        try:
            async with ctx.typing():
                api_url = f'https://www.countryflagicons.com/FLAT/64/{country}.png'

                embed = nextcord.Embed(title=f"Here's the flag of {country}",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_image(url=f"https://www.countryflagicons.com/FLAT/64/{country}.png")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find a flag related to {country}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def foodporn(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit('FoodPorn')
            top_posts = subreddit.hot(limit=100)

            FoodPorn = [post for post in top_posts if
                        not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

            if not FoodPorn:
                await ctx.send('No food found :(')
                return

            random_food = random.choice(FoodPorn)
            embed = nextcord.Embed(title=random_food.title, color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_image(url=random_food.url)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["rhymes"])
    async def rhyme(self, ctx, *, word):
        try:
            async with ctx.typing():
                query = word
                api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(query)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                embed = nextcord.Embed(title=f":notes: here are words that rhyme with {word}:",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                for values in response:
                    rhymes = values
                    embed.add_field(name="", value=f"{rhymes}")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: No rhymes found to {word}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["8ball"])
    async def ask(self, ctx, *, question):
        answers = [
            "Yes.",
            "No.",
            "Absolutely!",
            "Absolutely not",
            "Definitely no",
            "Definitely yes",
            "For sure",
            "Hell nah",
            "No way",
            "Positive.",
            "Negative."
        ]

        answer = random.choice(answers)

        embed = nextcord.Embed(title=f":8ball: {answer}",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=["roll"])
    async def dice(self, ctx):
        dice = random.randint(1, 6)

        embed = nextcord.Embed(title=f":game_die: You rolled the dice and got ``{dice}``",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=["flip"])
    async def coin(self, ctx):
        coin = random.choice(["heads", "tails"])

        embed = nextcord.Embed(title=f":coin: You flipped the coin and got ``{coin}``",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def advice(self, ctx):
        try:
            async with ctx.typing():
                api = "https://api.adviceslip.com/advice"
                response = requests.get(api).json()
                data = response

                id = response["slip"]["id"]
                advice = response["slip"]["advice"]

                embed = nextcord.Embed(title=f":information_source: Here's a random advice:",
                                       description=f"``{advice}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="ID:", value=f"{id}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: No advice for you",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def kanye(self, ctx):
        try:
            async with ctx.typing():
                api = "https://api.kanye.rest/"
                response = requests.get(api).json()
                data = response

                quote = data["quote"]

                embed = nextcord.Embed(title=f":performing_arts: Here's a random Kanye quote:",
                                       description=f"``{quote}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: No Kanye quotes found",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def fact(self, ctx):
        try:
            async with ctx.typing():
                api = f"https://api.api-ninjas.com/v1/facts?limit=1"
                response = requests.get(api, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                fact = info["fact"]

                embed = nextcord.Embed(title=f":grey_exclamation: Here's a random fact:",
                                       description=f"``{fact}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find anything any facts",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(fun(bot))
