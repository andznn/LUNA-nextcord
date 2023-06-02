"""
Config file for LUNA✱ Discord Bot
Created by Andrew
"""

import nextcord
from nextcord.ext import commands, tasks
import json
import random
import datetime
import colorama
from colorama import Fore, Style
import sys
from bot_token import token
from reddit_setup import *
from colors import *
from api_keys import *
from AnilistPython import Anilist
import aiohttp
import asyncio

token = token
version = "v0.5/2023"
pythonv = sys.version[:6]
nextcordv = nextcord.__version__
creator = "andzn"
now = datetime.datetime.now()
seperator = "-------------------------------------------------"
colorama.init()
anilist = Anilist()
helpGuide = json.load(open("help.json"))
us = 0
um = 0
uh = 0
ud = 0
