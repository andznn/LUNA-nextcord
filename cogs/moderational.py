"""
This is a cog file of LUNA✱ Containing moderational commands
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


class moderational(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def channel(self, ctx, option=None, type=None, *, name=None):
        if option is None and name is None:
            embed = nextcord.Embed(title=f":x: No option chosen!",
                                   description=f"Use one of the options below:",
                                   color=lunaorange, timestamp=ctx.message.created_at)
            embed.add_field(name="Create", value=f"`.channel create [type=voice or text][name]`")
            embed.add_field(name="More coming soon...", value=f"", inline=False)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
        elif option == "create":
            if type == "text":
                await ctx.guild.create_text_channel(name=f'{name}')
                embed = nextcord.Embed(title=f":white_check_mark: Channel created",
                                       description=f"Success!",
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            if type == "voice":
                await ctx.guild.create_voice_channel(name=f'{name}')
                embed = nextcord.Embed(title=f":white_check_mark: Channel created",
                                       description=f"Success!",
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
            else:
                embed = nextcord.Embed(title=f":x: Wrong channel type",
                                       description=f"Use .channel create voice/text [name]!",
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(title=f":x: No valid option provided",
                                   description=f"Use .channel to see available options",
                                   color=lunaorange, timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            
    @commands.command(aliases=["purge"], description="Purges provided amount of messages")
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        embed = nextcord.Embed(title=f":broom: Success!", description=f"Purged ``{amount}`` messages. *Deleting in 3s*",
                               color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed, delete_after=3)

    @commands.command(aliases=["hammer"], description="Bans tagged used from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = nextcord.Embed(title=f":hammer: {member} has been banned by {ctx.author}",
                               description=f"Reason: {reason}",
                               color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)
        await member.send(f"You have been banned from {ctx.guild.name} reason: {reason}")

    @commands.command(aliases=["forgive"], description="Unbans provided user")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command(aliases=["boot"], description="Kicks tagged user from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = nextcord.Embed(title=f":boom: {member} has been kicked by {ctx.author}",
                               description=f"Reason: {reason}",
                               color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)
        await member.send(f"You have been kicked from {ctx.guild.name} reason: {reason}")

    @commands.command(aliases=["timeout"], description="Timeout selected user")
    async def mute(self, ctx, member: nextcord.Member, *, reason=None):
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send("This command requires elevated permissions!")
            return
        guild = ctx.guild
        muteRole = nextcord.utils.get(guild.roles, name="Muted")

        if not muteRole:
            await ctx.send("No mute role found. Creating mute role...")
            muteRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(muteRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=True)
        await member.add_roles(muteRole, reason=reason)
        embed = nextcord.Embed(title=f":mute: {member} has been muted!",
                               description=f"Muted by {ctx.author.mention} on {now} for {reason}", color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)
        await member.send(f"You have been muted from **{guild.name}** for {reason}")

    @commands.command(description="Unmutes a member")
    async def unmute(self, ctx, member: nextcord.Member, *, reason=None):
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send("This command requires elevated permissions!")
            return

        guild = ctx.guild
        muteRole = nextcord.utils.get(guild.roles, name="Muted")

        if not muteRole:
            await ctx.send("The muted role has not been found")
            return

        await member.remove_roles(muteRole, reason=reason)
        embed = nextcord.Embed(title=f":mute: {member} has been unmuted!",
                               description=f"Unmuted by {ctx.author.mention} on {now}",
                               color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)
        await member.send(f"You have been unmuted from **{guild.name}!**")

    @commands.command(aliases=["slow", "sm"], description="Enables slowmode for chosen amount of time")
    async def slowmode(self, ctx, time: int):
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send("This command requires elevated permissions!")
            return
        try:
            if time == 0:
                embed = nextcord.Embed(title=f":stopwatch: Slowmode off",
                                       description=f"Disabled by {ctx.author.mention}",
                                       color=lunaorange, timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                await ctx.channel.edit(slowmode_delay=0)
            elif time > 21600:
                embed = nextcord.Embed(title=f":x: Slowmode cannot be greater than 6 hours!", color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                return
            else:
                embed = nextcord.Embed(title=f":stopwatch: Slowmode set to {time} seconds!",
                                       description=f"Applied by {ctx.author.mention} on {now}", color=lunaorange,
                                       timestamp=ctx.message.created_at)
                embed.set_footer(text=f"LUNA✱ ✦ Created by andzn",
                                 icon_url="https://i.ibb.co/yBXMVKG/icon.png")
                await ctx.send(embed=embed)
                await ctx.channel.edit(slowmode_delay=time)
        except Exception:
            await print("Something went wrong executing that command")

    @commands.command(aliases=["prefix"], description="Changes the bot prefix")
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.send("This command requires elevated permissions")
            return

        if prefix is None:
            prefix = "."

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        embed = nextcord.Embed(title=f":heavy_check_mark: Prefix changed!",
                               description=f"My prefix is now set to ``{prefix}``",
                               color=lunaorange, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["lockdown"])
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, channel: nextcord.TextChannel = None, setting=None):
        if setting == '--server':
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role,
                                              reason=f"{ctx.author.name} locked {channel.name} with --server",
                                              send_messages=False)
            embed = nextcord.Embed(title=f"Server locked!",
                                   description=f":lock: Server has been locked by {ctx.author.mention} on {now}",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            return
        if channel is None:
            channel = ctx.message.channel
        await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name}",
                                      send_messages=False)
        embed = nextcord.Embed(title=f"Channel locked!",
                               description=f":lock: Channel has been locked by {ctx.author.mention} on {now}",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, channel: nextcord.TextChannel = None, setting=None):
        if setting == '--server':
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role,
                                              reason=f"{ctx.author.name} unlocked {channel.name} with --server",
                                              send_messages=True)
            embed = nextcord.Embed(title=f"Server unlocked!",
                                   description=f":unlock: Server has been unlocked by {ctx.author.mention} on {now}",
                                   color=lunaorange,
                                   timestamp=ctx.message.created_at)
            embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
            await ctx.send(embed=embed)
            return
        if channel is None:
            channel = ctx.message.channel
        await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name}",
                                      send_messages=True)
        embed = nextcord.Embed(title=f"Channel unlocked!",
                               description=f":unlock: Channel has been unlocked by {ctx.author.mention} on {now}",
                               color=lunaorange,
                               timestamp=ctx.message.created_at)
        embed.set_footer(text=f"LUNA✱ ✦ Created by andzn", icon_url="https://i.ibb.co/yBXMVKG/icon.png")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(moderational(bot))
