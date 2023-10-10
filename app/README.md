# Looking Glass app
![Banner image](../img/banners/app-overview.png)
This is the mini app itself. It offers augmented reality features with a clean UI using some of Telegram's UI elements, and has a photo feature.

## Technical details
[A-Frame](https://aframe.io), a web-based 3D framework, is used for rendering 3D objects, and [AR.js](https://ar-js-org.github.io/AR.js/) is used for augmented reality.

The UI is built with pure HTML and CSS using modern HTML5 standards. For animation CSS transitions are used to make the code easier to understand.

For more information about the app's architecture see the [app overview](../docs/app/overview.md) page.

### Project structure
- [markers/](markers/) contains the markers used by the app.
- [models/](models/) contains the models used by the app.
- [lib/](lib/) contains some libraries used by the app:
    - [screenshot.js](lib/screenshot.js) is used for screenshots, as explained above.
    - [merge-images.js](lib/merge-images.js) is used by screenshot.js, as explained above.
    - [log-message.js](lib/log-message.js) adds a function for writing text into the developer console or to a visible log.
- [app.css](app.css) is the app's style sheet.
- [app.js](app.js) contains the app's code.
- [index.html](index.html) contains the layout of the app and the 3D scene.

## Acknowledgements
These are some of the 3D models and assets used in this project.
- ["Low Poly Car - Cadillac 75 Sedan 1953"](https://skfb.ly/op788) by ROH3D, licensed under [Creative Commons Attribution](http://creativecommons.org/licenses/by/4.0/).
- The marker for that model is a modified version of [Cadillac Fleetwood Limousine 1953](https://www.flickr.com/photos/8058098@N07/5629610212/) by [nakhon100](https://www.flickr.com/people/8058098@N07), licensed under [Creative Commons Attribution](http://creativecommons.org/licenses/by/2.0/).
- [Low poly Robot](https://poly.pizza/m/aEZGxB2ydPU) by Anastasiia Ku ([CC-BY](https://creativecommons.org/licenses/by/3.0/)) via Poly Pizza.

The project also uses the following 3rd party libraries:
- [screenshot.js](lib/screenshot.js), based on [this](https://github.com/jeromeetienne/AR.js/issues/358#issuecomment-716137205) comment, is used for taking photos
- that library uses [merge-images](https://github.com/lukechilds/merge-images) to merge screenshots of the camera feed and 3D objects