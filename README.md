# Looking Glass
![Banner image](img/banners/setup.png)
An augmented reality Telegram mini app. It can recognize various images, show AR experiences and let users take photos.

In the future, it will support markerless AR, interactive experiences and games as well.

## Try it out
[<img src="img/view_in_tg.png" width="300px" alt="View in Telegram">](https://t.me/LookingGlassARBot/arapp)

Note that a special image is required to use Looking Glass:

<img src="app/markers/bitbot/bitbot.png" height="650">

## Why AR?
I've seen a lot of companies make AR experiences that usually require their own apps. Let's face it, people are going to download such an app, look at the AR experience once, and forget that the app even exists until they run out of storage and get a reminder about an unused app that can be deleted.

In contrast to this, Telegram is one of the most popular messaging apps, so a lot of people are going to have it already. And since web AR technologies are capable enough to replace apps in these use cases no downloads are required.

## Repository structure
This repository consists of the mini app and its backend.
- The [app](app/) is built with A-Frame and AR.js and doesn't use any UI frameworks. It has a UI inspired by Telegram's mobile apps.
- The [backend](server/) is built with Python and has 2 parts:
    - An API built with Flask, which handles uploads of photos.
    - A Telegram bot built with python-telegram-bot, which shows the mini app to users and sends the images they take to them.
- The [documentation](docs/) contains information about both parts.

For more details check out the overview for the [app](docs/app/overview.md) and [backend](docs/server/overview.md) respectively.

## Setup
Follow the [setup guide](docs/setup.md).

## License
The app and server are licensed under the Mozilla Public License. If you fork the app, please credit the author (@githubcatw) in your documentation.