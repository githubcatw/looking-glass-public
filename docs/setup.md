# Setting up Looking Glass
![Banner image](../img/banners/setup.png)
This guide covers setting up the Looking Glass app and backend.

This guide was written with Linux and macOS in mind. If you're using Windows:
- replace `python3` with `python`,
- replace `pip3` with `pip`.

> If anything goes wrong during setup, check out the troubleshoot guides for the [app](app/troubleshoot.md) and [backend](server/troubleshoot.md).

## Requirements
Any moderately fast web server that has Python is enough. A separate web server might also be needed to host the Looking Glass app.

The live version is being hosted at Google App Engine.

## Pre-made configurations
The Looking Glass repository has pre-made configuration options for popular hosting services.

> If you aren't using a hosting service skip to [Do it yourself](#do-it-yourself).

### Google App Engine
The repository is configured to support Google App Engine. It might work with similar services (like Amazon EC2 or Heroku) with some changes.

Here is how to set up the Looking Glass backend and app in App Engine:

1. Fork this repository.
2. [Create a Google Cloud project.](https://console.cloud.google.com/projectcreate)
3. Enable billing.
4. Enable the following APIs:
    - [Identity and Access Management (IAM) API](https://console.cloud.google.com/flows/enableapi?apiid=iam.googleapis.com),
    - App Engine Admin API,
    - [Cloud Build API](https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com).
5. Go to [App Engine](https://console.cloud.google.com/appengine/start) and create an application.
6. Select a server region.
7. Wait until the application is created.
8. When asked to install the Google Cloud SDK, click "I'll do this later".
9. Go to the [Cloud Build triggers page](https://console.cloud.google.com/cloud-build/triggers) and create a trigger.
10. Give the trigger a name.
11. Under "Repository", click "Connect new repository" and connect your fork of Looking Glass.
12. Under "Configuration", select "Cloud Build configuration file (.yaml or .json)". There is no need to change the path.
13. Under "Substitution variables" in "Advanced", add the following variables:
    - **_BOT_TOKEN** - the bot token provided by BotFather.
    - **_APP_URL** - the URL of the Looking Glass **app**. Should be `https://[PROJECT_ID].[REGION_ID].r.appspot.com/app`.
        - Here:
            - `[PROJECT_ID]` is the project's ID. It's written in the URL and can be found on the Google Cloud dashboard.
            - `[REGION_ID]` is the region ID of the App Engine container.
    - **_SERVER_URL** - the URL of the Looking Glass **backend** (i.e. the server that is being set up). Should be `https://[PROJECT_ID].[REGION_ID].r.appspot.com/`.
    - **_PORT** - `8080`.

### Passenger
While Passenger isn't officially supported, a `passenger_wsgi.py` file that can be used to start the Looking Glass backend can be found [here](https://gist.github.com/githubcatw/4b3f8eef07a59137cf72a2e9ee36fe8e). To run the Looking Glass backend with Passenger, put that file in the folder this repository is in.

The Looking Glass app needs to be hosted separately or put in the `public` folder.

## Do it yourself
If you don't use a hosting platform or use an unsupported one, you can still set up Looking Glass.

First, download the Looking Glass repository or clone it using git; this folder will be known as the **root folder**.

### Setting up the Looking Glass backend
It's recommended to use a virtual environment to isolate Looking Glass's dependencies from the dependencies of other apps:
```bash
$ pip3 install virtualenv
$ virtualenv lgenv
# wait for the configuration to finish

# activate the virtual environment
$ source lgenv/bin/activate
# or, if you're on Windows:
> lgenv/Scripts/activate
```
If done correctly, the environment's name (`lgenv` in this example) should appear at the start of the line. Proceed with the guide.

1. Install the dependencies:
```bash
$ pip3 install -r requirements.txt
```

2. Set the required environment variables:
- **LG_BOT_TOKEN** - the bot token provided by BotFather.
- **LG_APP_URL** - the URL of the Looking Glass **app**.
- **LG_SERVER_URL** - the URL of the Looking Glass **backend** (i.e. the server that is being set up).
- **LG_SERVER_PORT** - the port to run the API on. Defaults to `8000`.
    - The port can be found in the documentation of the hosting service or configuration of the reverse proxy/port forwarding software. 
    - Some common ports include `8080` (used by Google App Engine and Amazon EC2) and `8000` (used by Azure).

3. Run the setup script:
```python
$ python3 setup.py
```
The setup script will configure the Looking Glass backend and app.

> If setting environment variables isn't possible, create a `.env` file with the variables instead or use `setup.py` with the `-e` flag to generate one from the current computer's environment variables: `python3 setup.py -e`.
> 
> Example:
> ```
> LG_BOT_TOKEN=1234567890:OxLM7ltZM53FLH2LGVlBOILclc9NGsEQ1bH
> LG_APP_URL=https://looking-glass.example/app
> LG_SERVER_URL=https://api.looking-glass.example
> LG_SERVER_PORT=8080
> ```
>
> Put the .env file in the root folder.

4. Start the backend:
```bash
$ python3 -m server
```
The backend will start, and you should see something like this:
```
INFO:     Waiting for application startup.
INFO:     ASGI 'lifespan' protocol appears unsupported.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

> Please do not use `flask run` to run the Looking Glass backend. It's OK for development but not recommended in any other case.

### Setting up the Looking Glass app
1. If the Looking Glass app won't be available at `/app` (i.e. `https://(your domain)/app`), open the app's HTML file (app/index.html) and replace `app/` with your folder's name.
> Note that this doesn't refer to the location of the `app` folder on the server, but to the URL of the app.
>
> Example, assuming Looking Glass will be available at `/public/app`:
> ```html
    <!-- define a marker - notice the "url" argument -->
    <a-nft
        type="nft"
        url="./public/app/markers/bitbot/bitbot"
        smooth="true"
        smoothCount="10"
        smoothTolerance=".01"
        smoothThreshold="5"
    >
        <!-- the model's URL doesn't need to be changed -->
        <a-entity
        gltf-model="models/robot/robot.glb"
        scale="150 150 150"
        position="0 0 0"></a-entity>
    </a-nft>
> ```

2. To host the app:
    - If you want to use the same server to host both the Looking Glass backend and app, configure it to host the app's folder as a **static folder**. For this, look in your hosting platform or web server/reverse proxy software's documentation.
    - If you want to use different servers for the backend and app, upload the `app/` folder to the server that will host the app.

## Setting up the bot
1. Create a new web app in BotFather with `/newapp`.
2. Select your bot.
3. Send the name and description of your app.
4. Send a photo for the app.
5. Send a demo GIF or skip that step.
    - The above 3 steps set up the preview that will be shown when the link to the mini app is shared.
6. When asked for the web app URL, send the URL of the Looking Glass **app**.
    - Don't send the URL of the Looking Glass backend.
7. Send a short name. It will be used in the link of the web app.

That's it. The Looking Glass app should appear when the t.me link sent by BotFather is tapped.
> If the Looking Glass GitHub repository appears instead, you've sent the URL of the backend. Use `/myapps` in BotFather to change the URL.

## Next steps
At this point, you should have a working version of Looking Glass.

You might want to replace the default images and models with your own. For that see the guide on [creating your own content](creating-markers.md).