"""
Looking Glass - server
Bot initialization
(c) 2023 githubcatw
"""

# Import Telegram related things
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application, TypeHandler

# Import the bot token from the main server file
from .. import BOT_TOKEN, APP_URL, SERVER_URL
from .. import PhotoUpdate, CustomContext

# Import the commands
from .greet import greet, set_web_app_url as set_url_for_greet
from .post import post_handler

# Placeholder for the app.
app = None

# Pass the web app URL to the greet command
set_url_for_greet(APP_URL)

"""
Posts a message.
"""
async def post(user_id, local_url):
    # Make a PhotoUpdate and add it to the queue
    await app.update_queue.put(WebhookUpdate(user_id=user_id, local_url=local_url))
    # Eventually it will be picked up by post_handler and the photo will be sent to the user

"""""
Sets the bot up.
"""
async def setup():
    global app
    # Create the bot in webhook mode
    context_types = ContextTypes(context=CustomContext)
    app = (
        Application.builder().token(BOT_TOKEN).context_types(context_types).updater(None).build()
    )
    # Register handler for /start
    app.add_handler(CommandHandler("start", greet))
    # Register handler for photo updates
    app.add_handler(TypeHandler(type=PhotoUpdate, callback=post_handler))

    # Pass webhook settings to telegram
    await app.bot.set_webhook(url=f"{SERVER_URL}/tg", allowed_updates=Update.ALL_TYPES)

"""
Gets the bot's Application.

It's recommended to use this function over importing bot.app so there are no
import issues. If bot.app is imported before it is set up by setup() (which
happens when the server is starting up), it will stay None, while this
function will always return the latest version.
"""
def get_app():
    return app