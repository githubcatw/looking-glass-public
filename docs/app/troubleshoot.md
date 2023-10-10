Like with any web app, the developer console and Google are your best friends when trying to fix an issue with the Looking Glass app. To enable developer tools in Telegram mini apps check the [instructions](https://core.telegram.org/bots/webapps#debug-mode-for-mini-apps) on Telegram's website.

Below are some common issues that might occur with the Looking Glass app and their solutions.

## The app doesn't load
This could happen because of several issues. The developer console can help.

### `GET (looking glass app server)/config.js net::ERR_ABORTED 404 (Not Found)` appears in the console
This means that the `config.js` file doesn't exist. It is created by `setup.py` when setting up the Looking Glass backend. Please see the [setup guide](../setup.md).

### The app gets stuck on the loading screen
In this case the last message in the console is usually `[info] Labeling mode set to 1`.

This could happen because of an issue with the URLs of the markers. Please see the section below.

## The app doesn't track custom markers
This might be caused by issues with the app's HTML file or the marker files.

### Troubleshooting the app
- Check the URL of the `a-nft` tag corresponding to your marker. It should be the path to your marker files without extensions.
    - Examples, assuming your marker files are called `kitten` and are in `/ar/markers/kitten`:
        - Incorrect - `/ar/markers/kitten/`, `/ar/markers/kitten/kitten.fset3`.
        - Correct - `/ar/markers/kitten/kitten`.
    - The path should point to the 3 files downloaded from the marker creator (fset3, iset, fset), not your image file.
    - Check if the path is accessible from your web browser - it might be hidden by the web server.
    - This error usually causes a message like this to appear in the developer console:
    ```
    Error in loading marker on Worker X {message: 'Request failed with status code 404', name: 'AxiosError', code: 'ERR_BAD_REQUEST', config: {…}, request: XMLHttpRequest, …}
    ```
- The AR objects might be too small for the marker's estimated size.
    - Try resizing the objects.
- The AR objects might be too far from the marker.
    - Try moving the objects to the zero point, which should place them on the marker: `position="0 0 0"`.

### Troubleshooting the marker
- The marker might be low quality.
    - This might be the case for 
    - Remember, more details and higher resolution = better tracking quality.
    - For more information check out [the AR.js documentation on markers](https://github.com/Carnaux/NFT-Marker-Creator/wiki/Creating-good-markers).

## Development tools
Besides the developer console, there are a few other developer tools that can be used to fix issues with the Looking Glass app.

### Visible logging
This is a feature that shows messages about various events happening. It can be used to troubleshoot actions.

<img src="img/log_message.png" alt="Text in a monospace font. There are 5 lines - the last 3 are 'Hello world!', 'Hiding autoplay screen' and 'Marker loaded'." width="500"/>

To enable it, add this line to the app's HTML file after the loader (a `div` with the `loader` class):
```html
<p id="logMessage"></p>
```

### [A-Frame Inspector](https://github.com/aframevr/aframe-inspector)
This is an A-Frame tool that can be used to check the 3D scene. It's especially useful for troubleshooting issues related to tracking.

<img src="https://user-images.githubusercontent.com/674727/50159991-fa540c80-028c-11e9-87f1-72c54e08d808.png" width="500"/>

Note that it might cause stability issues and only works on desktop.

To use it, simply add the `inspector` attribute to the `a-scene` element in the app's HTML file:
```html
<a-scene
    vr-mode-ui="enabled: false;"
    renderer="logarithmicDepthBuffer: true;"
    embedded
    inspector
    arjs="trackingMethod: best; sourceType: webcam;debugUIEnabled: false;"
>
<!-- ... -->
```

Then press `<ctrl> + <alt> + i` when the app is running and AR is visible (i.e. after the loading is finished and after tapping the screen) to open the inspector.

### Pinball marker
This isn't really a development tool, but it can be used to rule out marker issues.

Looking Glass comes with the default [AR.js pinball marker](https://raw.githubusercontent.com/AR-js-org/AR.js/master/aframe/examples/image-tracking/nft-video/pinball.jpg). To use it for a model, replace the URL with `markers/pinball/pinball`. Example:
```html
<a-nft
    type="nft"
    url="markers/pinball/pinball"
    smooth="true"
    smoothCount="10"
    smoothTolerance=".01"
    smoothThreshold="5"
>
    <!-- marker contents (models, lighting etc.) go here -->
</a-nft>
```