# ---------------------------------------------------- LUNA✱BOT --------------------------------------------------------
"""
This is a main file of LUNA✱ Discord Bot Created by Andrew
"""
# ----------------------------------------------------- Libraries ------------------------------------------------------
import nextcord
from nextcord.ext import *
from nextcord import *
import json
import random
import datetime
import colorama
from colorama import Fore, Style
import sys
from bot_token import token
from reddit_setup import *
from config.colors import lunaorange, lunablue
from api_keys import *
import aiohttp
import asyncio
from config.config import *
import requests
import dateutils
import os
import wikipedia
import time
import gtts
from gtts import gTTS
import logging
from bot import luna_bot
from time import time

# --------------------------------------------- Running the main bot file ----------------------------------------------
luna_bot()