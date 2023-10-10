"""
Looking Glass - server
Update listener for API
(c) 2023 githubcatw
"""

# Import the bot application
from .. import bot
# Import the required Flask classes
from flask import Blueprint, Response, request
from http import HTTPStatus
# Import the Update class
from telegram import Update

# Create the blueprint
flask_app = Blueprint('bot_endpoints', __name__)

"""Handle incoming bot updates from Telegram"""
@flask_app.post("/tg")  # type: ignore[misc]
async def telegram() -> Response:
    # Send the update to the bot application
    app = bot.get_app()
    await app.update_queue.put(Update.de_json(data=request.json, bot=app.bot))
    # The bot will process the update and respond to it.
    # All that's left for the API is to respond to Telegram's request with a successful response.
    return Response(status=HTTPStatus.OK)