# Looking Glass backend
![Banner image](../img/banners/server-overview.png)
This is the server-side program.

It runs the Telegram bot and a simple API for sending photos.

## Technical details
The backend is built with Python. Flask is used for the API, and python-telegram-bot is used for the bot.

For more information see the [overview](../docs/server/overview.md) page.

## Folder structure
- [api/](api/) contains the API code.
- [bot/](bot/) contains the bot code.
- [common/](common/) contains code used by both the API and bot, as well as code that can be reused by other Flask-based mini app backends.