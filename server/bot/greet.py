"""
Looking Glass - server
Greet command
(c) 2023 githubcatw
"""

# Import Telegram related things
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# The web app URL
WEB_APP_URL = ""

# The greeting that will be sent to people
GREETING = """
Hello!

Are you ready to experience the magical world of augmented reality in Telegram?

Then click on the button to launch Looking Glass!
"""

# Sets the web app URL. Used to avoid import issues.
def set_web_app_url(url):
    global WEB_APP_URL
    WEB_APP_URL = url

# Greets users and sends them a link to the mini app.
async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Reply to the message with:
    await update.message.reply_text(
        # the greeting text,
        GREETING,
        # a button...
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                # called "Enter AR"...
                text="Enter AR!",
                # and pointing to a link to the web app
                web_app=WebAppInfo(url=WEB_APP_URL),
            )
        ),
    )
