"""
Looking Glass - server
Post endpoint
(c) 2023 githubcatw
"""

# Import the bot module
from .. import bot
# Import PhotoUpdate
from ..common import PhotoUpdate
# Import the initialization data and image decoder libraries
from ..common import tg_init_data, image_decoder
# Import the bot token
from .. import BOT_TOKEN

# Import the required Flask classes
from flask import Blueprint, Response, request
from http import HTTPStatus
# Import tempfile (used for, well, temporary files)
import tempfile

# Create the blueprint
flask_app = Blueprint('post', __name__)

"""Send a photo to a user"""
@flask_app.post("/post")  # type: ignore[misc]
async def send() -> Response:
    # Get the sent image URL
    image_url = request.json["url"]
    # Try to load the initialization data
    try:
        init_data = tg_init_data.load_init_data(request.json["init"], BOT_TOKEN)
    # A ValueError indicates that the initialization data is invalid.
    except ValueError:
        print("Received invalid init data!")
        # Return a "bad request" error in that case.
        return Response(status=HTTPStatus.BAD_REQUEST)
    print("Valid init data received, continuing to process.")

    # Decode the image
    image = image_decoder.decode_data_url(image_url)
    # Get the user ID
    user_id = init_data["user"]["id"]
    # Create an update for the bot
    upd = PhotoUpdate(user_id, photo=image)
    # Send it to the bot application
    await bot.get_app().update_queue.put(upd)
    # The bot will process the update and send the photo
    
    return Response(status=HTTPStatus.OK)