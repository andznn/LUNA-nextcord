"""
This is a cog file of LUNA✱ Containing animal commands
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


class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cats"])
    async def cat(self, ctx, *, name):
        name = name
        api_url = 'https://api.api-ninjas.com/v1/cats?name={}'.format(name)
        response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
        info = response[0]
        name = info["name"]
        length = info["length"]
        family_friendly = info["family_friendly"]
        shedding = info["shedding"]
        general_health = info["general_health"]
        playfulness = info["playfulness"]
        children_friendly = info["children_friendly"]
        grooming = info["grooming"]
        intelligence = info["intelligence"]
        other_pets_friendly = info["other_pets_friendly"]
        min_weight = info["min_weight"]
        max_weight = info["max_weight"]
        min_life_expectancy = info["min_life_expectancy"]
        max_life_expectancy = info["max_life_expectancy"]
        image = info["image_link"]

        embed = nextcord.Embed(title=f":cat: Information about {name}",
                               description=f"Here's information about ``{name}``",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.add_field(name="Name:", value=f"{name}")
        embed.add_field(name="Length:", value=f"{length}")
        embed.add_field(name="Family Friendly:", value=f"{family_friendly}/5")
        embed.add_field(name="Shedding:", value=f"{shedding}/5")
        embed.add_field(name="General Health:", value=f"{general_health}/5")
        embed.add_field(name="Playfulness:", value=f"{playfulness}/5")
        embed.add_field(name="Children Friendly:", value=f"{children_friendly}/5")
        embed.add_field(name="Grooming", value=f"{grooming}/5")
        embed.add_field(name="Intelligence:", value=f"{intelligence}/5")
        embed.add_field(name="Other Pets Friendly:", value=f"{other_pets_friendly}/5")
        embed.add_field(name="Min Weight:", value=f"{min_weight}")
        embed.add_field(name="Max Weight:", value=f"{max_weight}")
        embed.add_field(name="Min Life Expectancy:", value=f"{min_life_expectancy}")
        embed.add_field(name="Max Life Expectancy:", value=f"{max_life_expectancy}")
        embed.set_image(url=image)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["dogs"])
    async def dog(self, ctx, *, name):
        name = name
        api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(name)
        response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
        info = response[0]
        name = info["name"]
        good_with_children = info["good_with_children"]
        good_with_other_dogs = info["good_with_other_dogs"]
        shedding = info["shedding"]
        grooming = info["grooming"]
        drooling = info["drooling"]
        coat_length = info["coat_length"]
        good_with_strangers = info["good_with_strangers"]
        playfulness = info["playfulness"]
        protectiveness = info["protectiveness"]
        trainability = info["trainability"]
        energy = info["energy"]
        barking = info["barking"]
        min_life_expectancy = info["min_life_expectancy"]
        max_life_expectancy = info["max_life_expectancy"]
        image = info["image_link"]

        embed = nextcord.Embed(title=f":dog: Information about {name}",
                               description=f"Here's information about ``{name}``",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.add_field(name="Name:", value=f"{name}")
        embed.add_field(name="Good With Children:", value=f"{good_with_children}/5")
        embed.add_field(name="Good With Other Dogs:", value=f"{good_with_other_dogs}/5")
        embed.add_field(name="Shedding:", value=f"{shedding}/5")
        embed.add_field(name="Grooming:", value=f"{grooming}/5")
        embed.add_field(name="Drooling:", value=f"{drooling}/5")
        embed.add_field(name="Coat Length:", value=f"{coat_length}/5")
        embed.add_field(name="Good With Strangers", value=f"{good_with_strangers}/5")
        embed.add_field(name="Playfulness:", value=f"{playfulness}/5")
        embed.add_field(name="Protectiveness:", value=f"{protectiveness}/5")
        embed.add_field(name="Trainability:", value=f"{trainability}/5")
        embed.add_field(name="Energy:", value=f"{energy}/5")
        embed.add_field(name="Braking:", value=f"{barking}/5")
        embed.add_field(name="Min Life Expectancy:", value=f"{min_life_expectancy}")
        embed.add_field(name="Max Life Expectancy:", value=f"{max_life_expectancy}")
        embed.set_image(url=image)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def randomfox(self, ctx):
        api_url = 'https://randomfox.ca/floof/'
        response = requests.get(api_url).json()
        info = response
        image = info["image"]

        embed = nextcord.Embed(title=f":fox: Here is a cute fox!",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_image(url=image)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def randomcat(self, ctx):
        api_url = 'https://api.thecatapi.com/v1/images/search/'
        response = requests.get(api_url).json()
        info = response[0]
        image = info["url"]

        embed = nextcord.Embed(title=f":cat: Here is a cute cat!",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_image(url=image)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["shiba"])
    async def randomshiba(self, ctx):
        api_url = 'https://shibe.online/api/shibes'
        response = requests.get(api_url).json()
        info = response[0]

        embed = nextcord.Embed(title=f":dog2: Here is a shiba!",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_image(url=info)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command()
    async def randomdog(self, ctx):
        api_url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(api_url).json()
        info = response
        image = info["message"]

        embed = nextcord.Embed(title=f":dog2: Here is a random cute dog!",
                               description=f"",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_image(url=image)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["frog"])
    async def randomfrog(self, ctx):
        subreddit = reddit.subreddit('frog')
        top_posts = subreddit.hot(limit=100)

        frog = [post for post in top_posts if
                not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        if not frog:
            await ctx.send('No frogs found :(')
            return

        random_frog = random.choice(frog)
        embed = nextcord.Embed(title=random_frog.title, color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_image(url=random_frog.url)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["capybara", "capy", "randomcapy"])
    async def randomcapybara(self, ctx):
        subreddit = reddit.subreddit('capybara')
        top_posts = subreddit.hot(limit=100)

        capybara = [post for post in top_posts if
                    not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        if not capybara:
            await ctx.send('No capybaras found :(')
            return

        random_capybara = random.choice(capybara)
        embed = nextcord.Embed(title=random_capybara.title, color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_image(url=random_capybara.url)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["dachshund", "dachshunds"])
    async def randomdachshund(self, ctx):
        subreddit = reddit.subreddit('dachshund')
        top_posts = subreddit.hot(limit=100)

        dachshund = [post for post in top_posts if
                     not post.stickied and post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        if not dachshund:
            await ctx.send('No dachshunds found :(')
            return

        random_dachshund = random.choice(dachshund)
        embed = nextcord.Embed(title=random_dachshund.title, color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_image(url=random_dachshund.url)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(animals(bot))
