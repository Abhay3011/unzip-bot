# Copyright (c) 2022 EDM115

import os

from pyrogram import idle
from . import unzipperbot
from config import Config

if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    unzipperbot.start()
    print("Bot is active now ! Join @EDM115bots")
    idle()
