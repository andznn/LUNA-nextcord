"""
This is a cog file of LUNA✱ Containing food commands
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


class food(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["calorie", "calories"])
    async def nutrition(self, ctx, *, name):
        try:
            async with ctx.typing():
                api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(name)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                name = info["name"]
                calories = info["calories"]
                serving_size_g = info["serving_size_g"]
                fat_total_g = info["fat_total_g"]
                fat_saturated_g = info["fat_saturated_g"]
                protein_g = info["protein_g"]
                sodium_mg = info["sodium_mg"]
                potassium_mg = info["potassium_mg"]
                cholesterol_mg = info["cholesterol_mg"]
                carbohydrates_total_g = info["carbohydrates_total_g"]
                fiber_g = info["fiber_g"]
                sugar_g = info["sugar_g"]

                embed = nextcord.Embed(title=f":avocado: Here are nutrition facts about {name}",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Name:", value=f"{name}")
                embed.add_field(name="Calories:", value=f"{calories}")
                embed.add_field(name="Serving (g):", value=f"{serving_size_g}")
                embed.add_field(name="Fat (g):", value=f"{fat_total_g}")
                embed.add_field(name="Saturated Fat (g):", value=f"{fat_saturated_g}")
                embed.add_field(name="Protein (g):", value=f"{protein_g}")
                embed.add_field(name="Sodium (mg):", value=f"{sodium_mg}")
                embed.add_field(name="Potassium (mg):", value=f"{potassium_mg}")
                embed.add_field(name="Cholesterol (mg):", value=f"{cholesterol_mg}")
                embed.add_field(name="Carbohydrates Total (g):", value=f"{carbohydrates_total_g}")
                embed.add_field(name="Fiber (g):", value=f"{fiber_g}")
                embed.add_field(name="Sugar (g):", value=f"{sugar_g}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any info about {name}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command(aliases=["cook"])
    async def recipe(self, ctx, *, query):
        try:
            async with ctx.typing():
                query = query
                api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
                response = requests.get(api_url, headers={"X-Api-Key": NINJAS_KEY}).json()
                info = response[0]
                title = info["title"]
                ingredients = info["ingredients"]
                servings = info["servings"]
                instructions = info["instructions"]

                embed = nextcord.Embed(title=f":cook: Recipe for {query}",
                                       description=f"Here's a recipe for ``{query}``",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Title:", value=f"{title}")
                embed.add_field(name="Ingredients:", value=f"{ingredients}")
                embed.add_field(name="Servings:", value=f"{servings}")
                embed.add_field(name="Instructions:", value=f"{instructions}")
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        except IndexError:
            embed = nextcord.Embed(title=f":x: Didn't find any info about {query}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)

    @commands.command()
    async def cocktail(self, ctx, type=None, *, query=None):
        if type == "search":
            try:
                async with ctx.typing():
                    api = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}"
                    response = requests.get(api).json()
                    data = response["drinks"][0]

                    name = data["strDrink"]
                    category = data["strCategory"]
                    alcoholic = data["strAlcoholic"]
                    glass = data["strGlass"]
                    instructions = data["strInstructions"]
                    image = data["strDrinkThumb"]
                    ingredient1 = data["strIngredient1"]
                    ingredient2 = data["strIngredient2"]
                    ingredient3 = data["strIngredient3"]
                    ingredient4 = data["strIngredient4"]
                    ingredient5 = data["strIngredient5"]
                    ingredient6 = data["strIngredient6"]
                    ingredient7 = data["strIngredient7"]
                    ingredient8 = data["strIngredient8"]
                    ingredient9 = data["strIngredient9"]
                    ingredient10 = data["strIngredient10"]
                    ingredient11 = data["strIngredient11"]
                    ingredient12 = data["strIngredient12"]
                    ingredient13 = data["strIngredient13"]
                    ingredient14 = data["strIngredient14"]
                    ingredient15 = data["strIngredient15"]
                    measure1 = data["strMeasure1"]
                    measure2 = data["strMeasure2"]
                    measure3 = data["strMeasure3"]
                    measure4 = data["strMeasure4"]
                    measure5 = data["strMeasure5"]
                    measure6 = data["strMeasure6"]
                    measure7 = data["strMeasure7"]
                    measure8 = data["strMeasure8"]
                    measure9 = data["strMeasure9"]
                    measure10 = data["strMeasure10"]
                    measure11 = data["strMeasure11"]
                    measure12 = data["strMeasure12"]
                    measure13 = data["strMeasure13"]
                    measure14 = data["strMeasure14"]
                    measure15 = data["strMeasure15"]

                    embed = nextcord.Embed(title=f":cocktail: Here's what I found about {query}:",
                                           description=f"",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}")
                    embed.add_field(name="Category:", value=f"{category}")
                    embed.add_field(name="Alcoholic:", value=f"{alcoholic}")
                    embed.add_field(name="Glass:", value=f"{glass}")
                    embed.add_field(name="Instructions:", value=f"{instructions}", inline=False)
                    embed.add_field(name="Ingredients:", value=f"", inline=False)
                    if measure1 is not None:
                        embed.add_field(name=f"{ingredient1}", value=f"{measure1}")
                    if measure2 is not None:
                        embed.add_field(name=f"{ingredient2}", value=f"{measure2}")
                    if measure3 is not None:
                        embed.add_field(name=f"{ingredient3}", value=f"{measure3}")
                    if measure4 is not None:
                        embed.add_field(name=f"{ingredient4}", value=f"{measure4}")
                    if measure5 is not None:
                        embed.add_field(name=f"{ingredient5}", value=f"{measure5}")
                    if measure6 is not None:
                        embed.add_field(name=f"{ingredient6}", value=f"{measure6}")
                    if measure7 is not None:
                        embed.add_field(name=f"{ingredient7}", value=f"{measure7}")
                    if measure8 is not None:
                        embed.add_field(name=f"{ingredient8}", value=f"{measure8}")
                    if measure9 is not None:
                        embed.add_field(name=f"{ingredient9}", value=f"{measure9}")
                    if measure10 is not None:
                        embed.add_field(name=f"{ingredient10}", value=f"{measure10}")
                    if measure11 is not None:
                        embed.add_field(name=f"{ingredient11}", value=f"{measure11}")
                    if measure12 is not None:
                        embed.add_field(name=f"{ingredient12}", value=f"{measure12}")
                    if measure13 is not None:
                        embed.add_field(name=f"{ingredient13}", value=f"{measure13}")
                    if measure14 is not None:
                        embed.add_field(name=f"{ingredient14}", value=f"{measure14}")
                    if measure15 is not None:
                        embed.add_field(name=f"{ingredient15}", value=f"{measure15}")

                    embed.set_image(url=image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    await ctx.send(embed=embed)

            except IndexError:
                embed = nextcord.Embed(title=f":x: Didn't find any info about {query}",
                                       description=f'Please try again!',
                                       color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        if type == "random":
            try:
                async with ctx.typing():
                    api = f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
                    response = requests.get(api).json()
                    data = response["drinks"][0]

                    name = data["strDrink"]
                    category = data["strCategory"]
                    alcoholic = data["strAlcoholic"]
                    glass = data["strGlass"]
                    instructions = data["strInstructions"]
                    image = data["strDrinkThumb"]
                    ingredient1 = data["strIngredient1"]
                    ingredient2 = data["strIngredient2"]
                    ingredient3 = data["strIngredient3"]
                    ingredient4 = data["strIngredient4"]
                    ingredient5 = data["strIngredient5"]
                    ingredient6 = data["strIngredient6"]
                    ingredient7 = data["strIngredient7"]
                    ingredient8 = data["strIngredient8"]
                    ingredient9 = data["strIngredient9"]
                    ingredient10 = data["strIngredient10"]
                    ingredient11 = data["strIngredient11"]
                    ingredient12 = data["strIngredient12"]
                    ingredient13 = data["strIngredient13"]
                    ingredient14 = data["strIngredient14"]
                    ingredient15 = data["strIngredient15"]
                    measure1 = data["strMeasure1"]
                    measure2 = data["strMeasure2"]
                    measure3 = data["strMeasure3"]
                    measure4 = data["strMeasure4"]
                    measure5 = data["strMeasure5"]
                    measure6 = data["strMeasure6"]
                    measure7 = data["strMeasure7"]
                    measure8 = data["strMeasure8"]
                    measure9 = data["strMeasure9"]
                    measure10 = data["strMeasure10"]
                    measure11 = data["strMeasure11"]
                    measure12 = data["strMeasure12"]
                    measure13 = data["strMeasure13"]
                    measure14 = data["strMeasure14"]
                    measure15 = data["strMeasure15"]

                    embed = nextcord.Embed(title=f":cocktail: Here's a random cocktail:",
                                           description=f"",
                                           color=lunaorange,
                                           timestamp=ctx.message.created_at)
                    embed.add_field(name="Name:", value=f"{name}")
                    embed.add_field(name="Category:", value=f"{category}")
                    embed.add_field(name="Alcoholic:", value=f"{alcoholic}")
                    embed.add_field(name="Glass:", value=f"{glass}")
                    embed.add_field(name="Instructions:", value=f"{instructions}", inline=False)
                    embed.add_field(name="Ingredients:", value=f"", inline=False)
                    if measure1 is not None:
                        embed.add_field(name=f"{ingredient1}", value=f"{measure1}")
                    if measure2 is not None:
                        embed.add_field(name=f"{ingredient2}", value=f"{measure2}")
                    if measure3 is not None:
                        embed.add_field(name=f"{ingredient3}", value=f"{measure3}")
                    if measure4 is not None:
                        embed.add_field(name=f"{ingredient4}", value=f"{measure4}")
                    if measure5 is not None:
                        embed.add_field(name=f"{ingredient5}", value=f"{measure5}")
                    if measure6 is not None:
                        embed.add_field(name=f"{ingredient6}", value=f"{measure6}")
                    if measure7 is not None:
                        embed.add_field(name=f"{ingredient7}", value=f"{measure7}")
                    if measure8 is not None:
                        embed.add_field(name=f"{ingredient8}", value=f"{measure8}")
                    if measure9 is not None:
                        embed.add_field(name=f"{ingredient9}", value=f"{measure9}")
                    if measure10 is not None:
                        embed.add_field(name=f"{ingredient10}", value=f"{measure10}")
                    if measure11 is not None:
                        embed.add_field(name=f"{ingredient11}", value=f"{measure11}")
                    if measure12 is not None:
                        embed.add_field(name=f"{ingredient12}", value=f"{measure12}")
                    if measure13 is not None:
                        embed.add_field(name=f"{ingredient13}", value=f"{measure13}")
                    if measure14 is not None:
                        embed.add_field(name=f"{ingredient14}", value=f"{measure14}")
                    if measure15 is not None:
                        embed.add_field(name=f"{ingredient15}", value=f"{measure15}")

                    embed.set_image(url=image)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    await ctx.send(embed=embed)

            except IndexError:
                embed = nextcord.Embed(title=f":x: Didn't find any cocktails",
                                       description=f'Please try again!',
                                       color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

                await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(title=f":x: No type selected, use .cocktail search/random [query]",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(food(bot))
