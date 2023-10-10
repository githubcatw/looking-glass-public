var loader;
var loadingScreen;
// Auto-playing video, which is what AR.js uses to display the camera feed, isn't allowed.
// This means that users will see an ugly play icon instead of a camera feed.
// Video can only be played after the user makes a gesture. However, gestures don't have
// to be on the player itself, and can happen on other elements. So, a message is shown that
// asks the user to tap the screen. This message is referred to as the "autoplay screen".
var autoplayScreen;
// Shutter button.
var photoButton;
// "Photo is developing" overlay.
var photoOverlay;

function sendScreenshot(url) {
    log("Screenshot received, sending...")
    // Create an object that will be sent to the server as JSON.
    var data = {
        // Add the initialization data and the URL to it.
        "url": url,
        "init": Telegram.WebApp.initData
    }
    // Send a request to the server.
    // SERVER_URL is provided by config.js, which will be on the page.
    fetch(SERVER_URL + "/post", {
        // Set the headers.
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // Make a POST request.
        method: "POST",
        // Convert the data object to JSON and send it as the body.
        body: JSON.stringify(data)
    })
    // Now, the request will be sent, and the photo should hopefully be sent by the backend to the user.
    .then(function(res){
        // Hide the photo overlay
        autoplayScreen.classList.add("hide");
        // TODO show success UI
        log("Success")
    })
    .catch(function(res){
        log("Error, please check the console")
        console.log(res)
    })
}

// Called by the shutter button.
function shutter() {
    log("Photo button pressed.")
    // Unhide the photo overlay
    autoplayScreen.classList.remove("hide");
    // After a second:
    setTimeout(function() {
        // Take a screenshot of the A-Frame scene and background video.
        takeScreenshot(sendScreenshot)
        // A timeout is necessary to hide a minor freeze caused by the screenshot function.
    }, 1000);
}

// Removes the loading screen and shows the autoplay screen.
function showAutoplayScreen() {
    // Remove the loading screen
    loadingScreen.remove();
    // Unhide the autoplay warning screen
    autoplayScreen.classList.remove("hide");
}

// Returns the showAutoplayScreen() function for use in timeouts.
// This is a bit ugly but necessary because of how timeouts work in JS.
function getAutoplayScreenShowFunction() {
    return showAutoplayScreen;
}
// See above.
function getDeleteLoaderFunction() {
    return function() {
        loader.remove();
    }
}

// Changes some of the UI to fit this platform.
function adaptUI() {
    // Get UI elements
    var autoplayCTA = document.getElementById("autoplayCTA");

    // If the app is running in a web version of Telegram, change the autoplay screen text
    if (Telegram.WebApp.platform == "web") {
        // Change "Tap on the screen" to "Click here"
        autoplayCTA.innerText = autoplayCTA.innerText.replace("Tap the screen", "Click here");
    }
}

// All of this needs to be run when the page has been loaded.
window.onload = function(){
    log("Looking Glass v1.0");

    // Get UI elements
    loader = document.getElementById("loader");
    loadingScreen = document.getElementById("loadingScreen");
    autoplayScreen = document.getElementById("autoplayScreen");
    photoButton = document.getElementById("photo");
    photoOverlay = document.getElementById("photoOverlay");

    // This function should be ran when all markers have been loaded
    window.addEventListener("arjs-nft-loaded", (event) => {
        // At this point, both A-Frame and the markers have been loaded, and AR can work.
        // However, we still need to persuade the user to interact with the page,
        // so we show the "tap anywhere to experience AR" screen.
        log("Marker loaded");

        // This adds the "hide" class to the "loading..." screen, starting the opacity transition from app.css
        loadingScreen.classList.add("hide");
        // Show the AR card after a second 
        setTimeout(getAutoplayScreenShowFunction(), 1000);

        // Expand the window
        Telegram.WebApp.expand();
    });

    // Here we detect the autoplay screen being clicked.
    autoplayScreen.addEventListener("click",
        function () {
            log("Hiding autoplay screen");
            // Get the camera feed player
            var thing = document.getElementById("arjs-video");
            // If it exists, play the feed video and hide the loader
            if (thing != null) {
                thing.play();
                // This adds the "hide" class to the loader, triggering the opacity transition from app.css
                loader.classList.add("hide");
                // The loader should be deleted after a second to make interactions work
                setTimeout(
                getDeleteLoaderFunction(), 1000);
            }
        },
        // Make sure that it only gets triggered once
        {once: true}
    );

    // Here we detect the photo button being clicked.
    photoButton.addEventListener("click", shutter);

    // Adapt the UI to this platform.
    adaptUI();
}