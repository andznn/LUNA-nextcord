"""
This is a cog file of LUNA✱ Containing Game commands
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


class game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tracker(self, ctx, game, platform, *, nickname):
        if game == "csgo":
            if platform == "steam":
                try:
                    async with ctx.typing():
                        api_url = f'https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{nickname}'
                        response = requests.get(api_url, headers={"TRN-Api-Key": TRN_KEY}).json()
                        data = response["data"]
                        platformD = data["platformInfo"]
                        slug = platformD["platformSlug"]
                        userid = platformD["platformUserId"]
                        nicknameD = platformD["platformUserHandle"]
                        try:
                            avatar = platformD["avatarUrl"]
                        except:
                            avatar = None
                        user = data["userInfo"]
                        countrycode = user["countryCode"]
                        segments = data["segments"][0]
                        stats = segments["stats"]
                        try:
                            playtime = stats["timePlayed"]["displayValue"]
                        except:
                            playtime = "-"
                        try:
                            trnscore = stats["score"]["displayValue"]
                        except:
                            trnscore = "-"
                        try:
                            kills = stats["kills"]["displayValue"]
                        except:
                            kills = "-"
                        try:
                            deaths = stats["deaths"]["displayValue"]
                        except:
                            deaths = "-"
                        try:
                            kd = stats["kd"]["displayValue"]
                        except:
                            kd = "-"
                        try:
                            damage = stats["damage"]["displayValue"]
                        except:
                            damage = "-"
                        try:
                            headshots = stats["damage"]["displayValue"]
                        except:
                            headshots = "-"
                        try:
                            dominations = stats["dominations"]["displayValue"]
                        except:
                            dominations = "-"
                        try:
                            shotsfired = stats["shotsFired"]["displayValue"]
                        except:
                            shotsfired = "-"
                        try:
                            shotshit = stats["shotsHit"]["displayValue"]
                        except:
                            shotshit = "-"
                        try:
                            accuracy = stats["shotsAccuracy"]["displayValue"]
                        except:
                            accuracy = "-"
                        try:
                            bombsplanted = stats["bombsPlanted"]["displayValue"]
                        except:
                            bombsplanted = "-"
                        try:
                            bombsdefused = stats["bombsDefused"]["displayValue"]
                        except:
                            bombsdefused = "-"
                        try:
                            mvp = stats["mvp"]["displayValue"]
                        except:
                            mvp = "-"
                        try:
                            wins = stats["wins"]["displayValue"]
                        except:
                            wins = "-"
                        try:
                            ties = stats["ties"]["displayValue"]
                        except:
                            ties = "-"
                        try:
                            lost = stats["losses"]["displayValue"]
                        except:
                            lost = "-"
                        try:
                            played = stats["matchesPlayed"]["displayValue"]
                        except:
                            played = "-"
                        try:
                            wl = stats["wlPercentage"]["displayValue"]
                        except:
                            wl = "-"
                        try:
                            hs = stats["headshotPct"]["displayValue"]
                        except:
                            hs = "-"

                        embed = nextcord.Embed(title=f":video_game: Here's {nicknameD}'s CS:GO profile",
                                               description=f"",
                                               color=lunaorange,
                                               timestamp=ctx.message.created_at)
                        embed.add_field(name="Nickname:", value=f"{nicknameD}", inline=False)
                        embed.add_field(name="Platform:", value=f"{slug}", inline=True)
                        embed.add_field(name="User ID:", value=f"{userid}", inline=True)
                        embed.add_field(name="Country:", value=f"{countrycode}", inline=True)
                        embed.add_field(name="Playtime:", value=f"{playtime}", inline=True)
                        embed.add_field(name="TRN Score:", value=f"{trnscore}", inline=True)
                        embed.add_field(name="Kills:", value=f"{trnscore}", inline=True)
                        embed.add_field(name="Deaths:", value=f"{deaths}", inline=True)
                        embed.add_field(name="K/D:", value=f"{kd}", inline=True)
                        embed.add_field(name="Damage:", value=f"{damage}", inline=True)
                        embed.add_field(name="Headshots:", value=f"{headshots}", inline=True)
                        embed.add_field(name="Dominations:", value=f"{dominations}", inline=True)
                        embed.add_field(name="Shots Fired:", value=f"{shotsfired}", inline=True)
                        embed.add_field(name="Shots Hit:", value=f"{shotshit}", inline=True)
                        embed.add_field(name="Accuracy:", value=f"{accuracy}", inline=True)
                        embed.add_field(name="Bombs Planted:", value=f"{bombsplanted}", inline=True)
                        embed.add_field(name="Bombs Defused:", value=f"{bombsdefused}", inline=True)
                        embed.add_field(name="MVPs:", value=f"{mvp}", inline=True)
                        embed.add_field(name="Wins:", value=f"{wins}", inline=True)
                        embed.add_field(name="Ties:", value=f"{ties}", inline=True)
                        embed.add_field(name="Losses:", value=f"{lost}", inline=True)
                        embed.add_field(name="Matches Played:", value=f"{played}", inline=True)
                        embed.add_field(name="W-L Ratio:", value=f"{wl}", inline=True)
                        embed.add_field(name="Headshot %:", value=f"{hs}", inline=True)
                        embed.add_field(name="Via:",
                                        value=f"https://tracker.gg/csgo/profile/steam/{nickname}/overview",
                                        inline=False)
                        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                        embed.set_image(url=avatar)
                        embed.set_thumbnail(
                            url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                        await ctx.send(embed=embed)
                except:
                    embed = nextcord.Embed(title=f":x: Didn't find that players profile",
                                           description=f'Please try again!',
                                           color=lunablue, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    embed.set_thumbnail(
                        url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                    await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f":x: Wrong platform, use `steam`",
                                       description=f'Please try again!',
                                       color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_thumbnail(
                    url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                await ctx.send(embed=embed)

        if game == "apex":
            if platform == "origin" or platform == "xbl" or platform == "psn":
                try:
                    async with ctx.typing():
                        api_url = f'https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{nickname}'
                        response = requests.get(api_url, headers={"TRN-Api-Key": TRN_KEY}).json()
                        data = response["data"]
                        platformD = data["platformInfo"]
                        slug = platformD["platformSlug"]
                        nicknameD = platformD["platformUserHandle"]
                        metadata = data["metadata"]
                        try:
                            season = metadata["currentSeason"]
                        except:
                            season = "'"
                        try:
                            legend = metadata["activeLegendName"]
                        except:
                            legend = "-"
                        segments = data["segments"][0]
                        stats = segments["stats"]
                        try:
                            level = stats["level"]["displayValue"]
                        except:
                            level = "-"
                        try:
                            kills = stats["kills"]["displayValue"]
                        except:
                            kills = "-"
                        try:
                            damage = stats["damage"]["displayValue"]
                        except:
                            damage = "-"
                        try:
                            headshots = stats["headshots"]["displayValue"]
                        except:
                            headshots = "-"
                        try:
                            sniperKills = stats["sniperKills"]["displayValue"]
                        except:
                            sniperKills = "-"
                        try:
                            rank = stats["rankScore"]["displayName"]
                        except:
                            rank = "-"
                        try:
                            arenaRank = stats["arenaRankScore"]["displayName"]
                        except:
                            arenaRank = "-"
                        try:
                            arenaKills = stats["arenaSeason9Kills"]["displayValue"]
                        except:
                            arenaKills = "-"
                        try:
                            arenaWins = stats["arenaSeason9Wins"]["displayValue"]
                        except:
                            arenaWins = "-"
                        try:
                            wins = stats["wins"]["displayValue"]
                        except:
                            wins = "-"
                        try:
                            peakrank = stats["peakRankScore"]["displayName"]
                        except:
                            peakrank = "-"
                        try:
                            rankIcon = stats["rankScore"]["metadata"]["iconUrl"]
                        except:
                            rankIcon = "-"

                        embed = nextcord.Embed(title=f":video_game: Here's {nicknameD}'s Apex Legends profile",
                                               description=f"",
                                               color=lunaorange,
                                               timestamp=ctx.message.created_at)
                        embed.add_field(name="Nickname:", value=f"{nicknameD}", inline=False)
                        embed.add_field(name="Platform:", value=f"{slug}", inline=True)
                        embed.add_field(name="Season:", value=f"{season}", inline=True)
                        embed.add_field(name="Top Legend:", value=f"{legend}", inline=True)
                        embed.add_field(name="Level:", value=f"{level}", inline=True)
                        embed.add_field(name="Kills:", value=f"{kills}", inline=True)
                        embed.add_field(name="Damage:", value=f"{damage}", inline=True)
                        embed.add_field(name="Headshots:", value=f"{headshots}", inline=True)
                        embed.add_field(name="Sniper Kills:", value=f"{sniperKills}", inline=True)
                        embed.add_field(name="Rank:", value=f"{rank}", inline=True)
                        embed.add_field(name="Arena Rank:", value=f"{arenaRank}", inline=True)
                        embed.add_field(name="Arena Kills:", value=f"{arenaKills}", inline=True)
                        embed.add_field(name="Arena Wins:", value=f"{arenaWins}", inline=True)
                        embed.add_field(name="Wins:", value=f"{wins}", inline=True)
                        embed.add_field(name="Peak Rank:", value=f"{peakrank}", inline=True)
                        embed.add_field(name="Via:",
                                        value=f"https://apex.tracker.gg/apex/profile/{platform}/{nickname}/overview",
                                        inline=False)
                        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                        embed.set_image(url=rankIcon)
                        embed.set_thumbnail(
                            url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                        await ctx.send(embed=embed)
                except:
                    embed = nextcord.Embed(title=f":x: Didn't find that players profile",
                                           description=f'Please try again!',
                                           color=lunablue, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    embed.set_thumbnail(
                        url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                    await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f":x: Wrong platform, use `origin, xbl or psn`",
                                       description=f'Please try again!',
                                       color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_thumbnail(
                    url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                await ctx.send(embed=embed)

        if game == "division2":
            if platform == "uplay" or platform == "xbl" or platform == "psn":
                try:
                    async with ctx.typing():
                        api_url = f'https://public-api.tracker.gg/v2/division-2/standard/profile/{platform}/{nickname}'
                        response = requests.get(api_url, headers={"TRN-Api-Key": TRN_KEY}).json()
                        data = response["data"]
                        platformD = data["platformInfo"]
                        slug = platformD["platformSlug"]
                        nicknameD = platformD["platformUserHandle"]
                        avatar = platformD["avatarUrl"]
                        segments = data["segments"][0]
                        stats = segments["stats"]
                        try:
                            playtime = stats["timePlayed"]["displayValue"]
                        except:
                            playtime = "-"
                        try:
                            pvpKills = stats["killsPvP"]["displayValue"]
                        except:
                            pvpKills = "-"
                        try:
                            npcKills = stats["killsNpc"]["displayValue"]
                        except:
                            npcKills = "-"
                        try:
                            killsSkill = stats["killsSkill"]["displayValue"]
                        except:
                            killsSkill = "-"
                        try:
                            headshots = stats["headshots"]["displayValue"]
                        except:
                            headshots = "-"
                        try:
                            itemsLooted = stats["itemsLooted"]["displayValue"]
                        except:
                            itemsLooted = "-"
                        try:
                            totalXp = stats["xPTotal"]["displayValue"]
                        except:
                            totalXp = "-"
                        try:
                            clanXp = stats["xPClan"]["displayValue"]
                        except:
                            clanXp = "-"
                        try:
                            specialization = stats["specialization"]["displayValue"]
                        except:
                            specialization = "-"
                        try:
                            eCredits = stats["eCreditBalance"]["displayValue"]
                        except:
                            eCredits = "-"
                        try:
                            commendationCount = stats["commendationCount"]["displayValue"]
                        except:
                            commendationCount = "-"
                        try:
                            commendationScore = stats["commendationScore"]["displayValue"]
                        except:
                            commendationScore = "-"
                        try:
                            latestGearScore = stats["latestGearScore"]["displayValue"]
                        except:
                            latestGearScore = "-"
                        try:
                            highestPlayerLevel = stats["highestPlayerLevel"]["displayValue"]
                        except:
                            highestPlayerLevel = "-"
                        try:
                            xPPve = stats["xPPve"]["displayValue"]
                        except:
                            xPPve = "-"
                        try:
                            xPPvP = stats["xPPvP"]["displayValue"]
                        except:
                            xPPvP = "-"
                        try:
                            killsBurning = stats["killsBurning"]["displayValue"]
                        except:
                            killsBurning = "-"
                        try:
                            killsShocked = stats["killsShocked"]["displayValue"]
                        except:
                            killsShocked = "-"
                        try:
                            killsEnsnare = stats["killsEnsnare"]["displayValue"]
                        except:
                            killsEnsnare = "-"
                        try:
                            killsHeadshot = stats["killsHeadshot"]["displayValue"]
                        except:
                            killsHeadshot = "-"
                        try:
                            itemsLootedPerMin = stats["itemsLootedPerMin"]["displayValue"]
                        except:
                            itemsLootedPerMin = "-"
                        try:
                            playersKilled = stats["playersKilled"]["displayValue"]
                        except:
                            playersKilled = "-"

                        embed = nextcord.Embed(title=f":video_game: Here's {nicknameD}'s The Division 2 profile",
                                               description=f"",
                                               color=lunaorange,
                                               timestamp=ctx.message.created_at)
                        embed.add_field(name="Nickname:", value=f"{nicknameD}", inline=False)
                        embed.add_field(name="Platform:", value=f"{slug}", inline=True)
                        embed.add_field(name="Playtime:", value=f"{playtime}", inline=True)
                        embed.add_field(name="PVP Kills:", value=f"{pvpKills}", inline=True)
                        embed.add_field(name="NPC Kills:", value=f"{npcKills}", inline=True)
                        embed.add_field(name="Skill Kills:", value=f"{killsSkill}", inline=True)
                        embed.add_field(name="Headshots:", value=f"{headshots}", inline=True)
                        embed.add_field(name="Items Looted:", value=f"{itemsLooted}", inline=True)
                        embed.add_field(name="Items Looted/Min:", value=f"{itemsLootedPerMin}", inline=True)
                        embed.add_field(name="Total XP:", value=f"{totalXp}", inline=True)
                        embed.add_field(name="Clan XP:", value=f"{clanXp}", inline=True)
                        embed.add_field(name="Specialization:", value=f"{specialization}", inline=True)
                        embed.add_field(name="eCredits:", value=f"{eCredits}", inline=True)
                        embed.add_field(name="Commendations:", value=f"{commendationCount}", inline=True)
                        embed.add_field(name="Commendation Score:", value=f"{commendationScore}", inline=True)
                        embed.add_field(name="Latest Gear Score:", value=f"{latestGearScore}", inline=True)
                        embed.add_field(name="Highest Player Level:", value=f"{highestPlayerLevel}", inline=True)
                        embed.add_field(name="PVP XP:", value=f"{xPPvP}", inline=True)
                        embed.add_field(name="PVE XP:", value=f"{xPPve}", inline=True)
                        embed.add_field(name="Burning Kills:", value=f"{killsBurning}", inline=True)
                        embed.add_field(name="Shocked Kills:", value=f"{killsShocked}", inline=True)
                        embed.add_field(name="Ensnare Kills:", value=f"{killsEnsnare}", inline=True)
                        embed.add_field(name="Headshot Kills:", value=f"{killsHeadshot}", inline=True)
                        embed.add_field(name="Player Kills:", value=f"{playersKilled}", inline=True)
                        embed.add_field(name="Via:",
                                        value=f"https://tracker.gg/division-2/profile/{platform}/{nickname}/overview",
                                        inline=False)
                        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                        embed.set_image(url=avatar)
                        embed.set_thumbnail(
                            url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                        await ctx.send(embed=embed)
                except:
                    embed = nextcord.Embed(title=f":x: Didn't find that players profile",
                                           description=f'Please try again!',
                                           color=lunablue, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                    embed.set_thumbnail(
                        url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                    await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f":x: Wrong platform, use `origin, xbl or psn`",
                                       description=f'Please try again!',
                                       color=lunablue, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_thumbnail(
                    url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
                await ctx.send(embed=embed)

    @commands.command()
    async def league(self, ctx, platform, *, query):
        if platform == "BR1" or platform == "EUN1" or platform == "EUW1" or platform == "JP1" or platform == "KR" or platform == "LA1" or platform == "LA2" or platform == "NA1" or platform == "OC1" or platform == "RU":
            async with ctx.typing():
                api = f"https://{platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{query}"
                headers = {
                    "User-Agent": f"{RIOT_AGENT}",
                    "Accept-Language": f"{RIOT_LANGUAGE}",
                    "Accept-Charset": f"{RIOT_CHARSET}",
                    "Origin": f"{RIOT_ORIGIN}",
                    "X-Riot-Token": f"{RIOT_KEY}"
                }
                response = requests.get(api, headers=headers).json()
                id = response["id"]
                accId = response["accountId"]
                puuId = response["puuid"]
                name = response["name"]
                profileiconid = response["profileIconId"]
                level = response["summonerLevel"]
                print(response)

                mastery = f"https://{platform}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{id}"
                headers = {
                    "User-Agent": f"{RIOT_AGENT}",
                    "Accept-Language": f"{RIOT_LANGUAGE}",
                    "Accept-Charset": f"{RIOT_CHARSET}",
                    "Origin": f"{RIOT_ORIGIN}",
                    "X-Riot-Token": f"{RIOT_KEY}"
                }
                masteries = requests.get(mastery, headers=headers).json()

                embed = nextcord.Embed(title=f":video_game: Here's {query}'s League of Legends stats",
                                       description=f"",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Nickname:", value=f"{name}", inline=True)
                embed.add_field(name="Level:", value=f"{level}", inline=True)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_image(
                    url=f"http://ddragon.leagueoflegends.com/cdn/13.11.1/img/profileicon/{profileiconid}.png")
                await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(
                title=f":x: Wrong platform, use `BR1, EUN1, EUW1, JP1, KR, LA1, LA2, NA1, OC1 or RU`",
                description=f'Please try again!',
                color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            embed.set_thumbnail(
                url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/oprewpx3u3d8pwlu1mgb")
            await ctx.send(embed=embed)

    @commands.command()
    async def champion(self, ctx, *, query):
        try:
            async with ctx.typing():
                api = f"http://ddragon.leagueoflegends.com/cdn/13.11.1/data/en_US/champion/{query}.json"
                headers = {
                    "User-Agent": f"{RIOT_AGENT}",
                    "Accept-Language": f"{RIOT_LANGUAGE}",
                    "Accept-Charset": f"{RIOT_CHARSET}",
                    "Origin": f"{RIOT_ORIGIN}",
                    "X-Riot-Token": f"{RIOT_KEY}"
                }
                response = requests.get(api, headers=headers).json()
                data = response["data"]
                print(data)
                champion = data[f"{query}"]
                name = champion["name"]
                title = champion["title"]
                image = f"http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{query}_0.jpg"
                lore = champion["lore"]
                hp = champion["stats"]["hp"]
                movespeed = champion["stats"]["movespeed"]
                armor = champion["stats"]["armor"]
                mr = champion["stats"]["spellblock"]
                range = champion["stats"]["attackrange"]
                ad = champion["stats"]["attackdamage"]
                attackspeed = champion["stats"]["attackspeed"]
                passiveName = champion["passive"]["name"]
                passiveDescription = champion["passive"]["description"]
                Q = champion["spells"][0]
                qName = Q["name"]
                qDescription = Q["description"]
                W = champion["spells"][1]
                wName = W["name"]
                wDescription = W["description"]
                E = champion["spells"][2]
                eName = E["name"]
                eDescription = E["description"]
                R = champion["spells"][3]
                rName = R["name"]
                rDescription = R["description"]
                embed = nextcord.Embed(title=f"{name}",
                                       description=f"{title}",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Tags:", value=f"", inline=True)
                for k in champion["tags"]:
                    embed.add_field(name="", value=f"`{k}`", inline=True)
                embed.add_field(name="HP:", value=f"{hp}", inline=True)
                embed.add_field(name="MS:", value=f"{movespeed}", inline=True)
                embed.add_field(name="Armor:", value=f"{armor}", inline=True)
                embed.add_field(name="MR:", value=f"{mr}", inline=True)
                embed.add_field(name="Range:", value=f"{range}", inline=True)
                embed.add_field(name="AD:", value=f"{ad}", inline=True)
                embed.add_field(name="Attack Speed:", value=f"{attackspeed}", inline=True)
                embed.add_field(name="Skills:", value=f"", inline=False)
                embed.add_field(name=f"Passive: `{passiveName}`", value=f"{passiveDescription}", inline=False)
                embed.add_field(name=f"Q: `{qName}`", value=f"{qDescription}", inline=False)
                embed.add_field(name=f"W: `{wName}`", value=f"{wDescription}", inline=False)
                embed.add_field(name=f"E: `{eName}`", value=f"{eDescription}", inline=False)
                embed.add_field(name=f"R: `{rName}`", value=f"{rDescription}", inline=False)
                embed.add_field(name="Lore:", value=f"{lore[:1000]}...", inline=False)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                embed.set_image(url=image)
                embed.set_thumbnail(url=f"http://ddragon.leagueoflegends.com/cdn/13.11.1/img/champion/{query}.png")
                await ctx.send(embed=embed)
        except:
            embed = nextcord.Embed(title=f":x: Didn't find anything about {query}",
                                   description=f'Please try again!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)

    @commands.command()
    async def skin(self, ctx, champion, *, skin: int):
        try:
            async with ctx.typing():
                api = f"http://ddragon.leagueoflegends.com/cdn/13.11.1/data/en_US/champion/{champion}.json"
                headers = {
                    "User-Agent": f"{RIOT_AGENT}",
                    "Accept-Language": f"{RIOT_LANGUAGE}",
                    "Accept-Charset": f"{RIOT_CHARSET}",
                    "Origin": f"{RIOT_ORIGIN}",
                    "X-Riot-Token": f"{RIOT_KEY}"
                }
                response = requests.get(api, headers=headers).json()
                data = response["data"][f"{champion}"]
                lore = data["lore"]
                count = (len(data["skins"]))
                try:
                    skins = data["skins"][skin - 1]
                except:
                    skins = None
                try:
                    name = data["skins"][skin - 1]["name"]
                except:
                    skins = None
                try:
                    chromas = data["skins"][skin - 1]["chromas"]
                except:
                    chromas = None
                try:
                    num = data["skins"][skin - 1]["num"]
                except:
                    num = 0
                image = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion}_{num}.jpg"

                embed = nextcord.Embed(title=f"{name}",
                                       description=f"Skin {num + 1}/{count}",
                                       color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.add_field(name="Chromas:", value=f"{chromas}", inline=True)
                embed.add_field(name=f"{champion} Lore:", value=f"{lore[:1000]}...", inline=False)
                embed.set_image(url=image)
                embed.set_thumbnail(url=f"http://ddragon.leagueoflegends.com/cdn/13.11.1/img/champion/{champion}.png")
                await ctx.send(embed=embed)
        except:
            embed = nextcord.Embed(title=f":x: Didn't find that skin",
                                   description=f'{champion} has only {count} skins!',
                                   color=lunablue, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(game(bot))
