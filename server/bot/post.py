"""
Looking Glass - server
Post commands for bot
(c) 2023 githubcatw
"""

# Import Telegram related things
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

from . import PhotoUpdate

"""
Receives photo updates and sends the photos to their authors.
"""
async def post_handler(update: PhotoUpdate, context: CallbackContext) -> None:
    # Message the user that took the photo
    await context.bot.send_photo(
        update.user_id,
        photo=update.photo,
        caption="Here's the photo you took in Looking Glass.\n\nIf you want to jump back in, press the \"Start AR\" button."
    )
    # Close and delete the temporary file once the message has been sent
    update.photo.close()