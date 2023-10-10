# Backend overview
![Banner image](../../img/banners/server-overview.png)
The Looking Glass backend is built with Flask and python-telegram-bot. It handles 2 main features:
- directing users that start the bot to the Looking Glass app,
- sending photos taken by users to them.

## Architecture
> A full documentation of custom functions in the backend code can be found in the [functions](functions.md) page.
The 2 main components - the API and bot - are placed in different submodules. There is also a `common` submodule containing some code used in both parts.

The API is built like a regular Flask app, using blueprints to configure endpoints.

The bot is built slightly differently compared to regular bots built with python-telegram-bot. By default, python-telegram-bot creates an `Updater` to check for incoming updates (i.e. messages, status changes...) from Telegram. This is fine if the only thing that the server needs to run is the bot, but in this case it's also running an API, which causes conficts.

To avoid complicating the code the bot is instead started in [webhook mode](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks). This means that the API receives incoming updates and sends them to python-telegram-bot to process and respond to.

### Directing users to the Looking Glass app
This is done with a regular `CommandHandler`, just like in any other bot. `ReplyKeyboardMarkup` is used to show a button for the Looking Glass app.

### Sending photos
The shutter button in the Looking Glass app sends a web request to the backend. If you're interested in the details of the implementation of the shutter button check out the relevant part in the [app overview](../app/overview.md).

The API first verifies the received data according to [Telegram's documentation](https://core.telegram.org/bots/webapps#validating-data-received-via-the-mini-app). If it's valid, it saves the image from the sent data link and sends a custom update to the bot.

The bot processes this update and sends a message with the photo attached to the person that took it, provided that they have allowed the bot to send messages to them.