Like with any Python app, the terminal and Google are your best friends when trying to fix an issue with the Looking Glass backend.

Below are some common issues that might occur with the Looking Glass backend and their solutions.

## Issues that occur during setup
These errors cause `setup.py` to fail.

### `AssertionError: The LG_SERVER_URL variable isn't set. Please set it to start this script.`
This means that the environment variable `LG_SERVER_URL` isn't set. Please check if it's set and keep in mind that setup doesn't support `.env` files.

If it's not possible to set `LG_SERVER_URL`, the script also supports `_LG_SERVER_URL`.

If the variables are set and this is happening on a cloud app hosting solution (such as Google App Engine or Amazon EC2) try removing the space between the "=" sign in your build file (e.g. `clouduild.yaml` for Google Cloud Build). Example:
```yaml
# before:
'LG_SERVER_URL = https://looking-glass.example'
# after:
'LG_SERVER_URL=https://looking-glass.example'
```

## Issues that occur during startup
These errors cause the backend to crash when it's starting.

### `Looking Glass can't work without the environment variable [...] being set.`
This means that a required environment variable isn't set. Please check the setup guide.

On cloud app hosting solutions with no easy way to pass environment variables to running apps [setup.py](/setup.py) can be used with the `-e` flag (i.e. `python3 setup.py -e`) in the build step. This will generate a `.env` file that can be used by the backend instead of environment variables when it's running. To work around naming limitations on some platforms it also accepts variables starting with underscores (e.g. `_LG_SERVER_PORT` instead of `LG_SERVER_PORT`). Check the [app.yaml](/app.yaml) file for a usage example.

Note: **never share the generated .env file**, as an attacker might use it to **take over the bot or hijack the app**.

> If the error remains after using that script and the variables are correct, check the build logs. The script logs the names of variables that get added to the `.env` file; make sure that all required variables get added.

## Issues that occur during runtime
These errors appear when the backend is running and might crash it or cause other unintended behavior.

### The bot doesn't respond to messages
Check the server URL (set with the environment variable `LG_SERVER_URL`) - it must be the URL of the backend, **not** the web app (the one that gets launched by your bot).

### The bot keeps sending the same messages over and over again
This, especially if the messages are sent around once every minute, means that an error has occured in either the bot's code or the part of the API's code which sends updates to the bot. Please check the logs for more information.

### `telegram.error.InvalidToken: Not Found`
This means that the bot token (set with the environment variable `LG_BOT_TOKEN`) is incorrect. Please check if that variable has the correct token for your bot.

### Photos aren't sent and `Invalid init data` appears in the console
The initialization data sent by Telegram can be considered invalid by the backend for numerous reasons.

A really common problem that causes this issue is the bot token being incorrect. Make sure that the token the Looking Glass backend is set up with matches the bot you're starting the Looking Glass app with.