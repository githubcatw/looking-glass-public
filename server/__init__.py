"""
Looking Glass - server
Initialization script
(c) 2023 githubcatw
"""

# Import all common classes
from .common import *


# Environment variables are loaded here to not cause issues with
# the bot and API modules.

# Import the environment variable methods
from .common.env import get_env_or_exit
import os

# Load variables from the .env file, if it exists
from dotenv import load_dotenv
# load_dotenv() returns if it was successful - in that case print a message
if load_dotenv():
    print("Loaded .env file successfully.")
    # Check if the .env file has been loaded by testing the bot token variable
    test = os.environ.get("LG_BOT_TOKEN", None)
    if test == None:
        print("Self test: bot token is UNSET - this will cause an error")
    else:
        print("Self test: bot token is set")

# Load required environment variables
BOT_TOKEN = get_env_or_exit("LG_BOT_TOKEN")
APP_URL = get_env_or_exit("LG_APP_URL")
SERVER_URL = get_env_or_exit("LG_SERVER_URL")

# Load optional environment variables
PORT = os.environ.get("LG_SERVER_PORT", 8080)


# Import the start functions for the bot and API
from .bot import setup as setup_bot, get_app as get_bot_app
from .api import create_ws

# Import asyncio for the start function
import asyncio

async def startAsync():
    # Setup the Telegram bot
    await setup_bot()
    # Create a web server instance
    webserver = create_ws()

    # Get the bot app after setup
    bot_app = get_bot_app()
    # Run bot application and webserver together
    async with bot_app:
        # Start the bot first
        print("Starting bot...")
        await bot_app.start() #doesn't impact
        # Then the web server
        await webserver.serve()
        
        # When the server has stopped, stop the bot too
        print("Stopping bot...")
        await bot_app.stop()

def start():
    asyncio.run(startAsync())