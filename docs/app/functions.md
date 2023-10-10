# App functions
![Banner image](../../img/banners/app-structure.png)
This document is documentation for all functions in the Looking Glass app, including the main source code and all custom libraries.

## Libraries

### Screenshots (`screenshot.js`)
This library manages taking photos.

#### `resizeCanvas(origCanvas, width, height)`
Resizes the given canvas's contents to the given width and height.

**Arguments:**
| Name         | Meaning              |
|--------------|----------------------|
| `origCanvas` | the canvas to resize |
| `width`      | the new width        |
| `height`     | the new height       |

**Returns:** a `data:` URL to the resized image.

#### `captureVideoFrame(video, format, width, height)`
Captures the current frame of a given `video` element.

**Arguments:**
| Name     | Meaning                                                       |
|----------|---------------------------------------------------------------|
| `video`  | the `video` element to capture                                |
| `format` | the image format, either `jpeg` or `png` - defaults to `jpeg` |
| `width`  | the capture width, defaults to the video's width              |
| `height` | the capture height, defaults to the video's height            |

**Returns:** a `data:` URL to the resized image.

#### `takeScreenshot(callback)`
Takes a photo of the 3D frame and camera feed and calls the callback function with the `data:` URL as the argument.

**Argument:** `callback` - the callback function.

**Example:**
Takes a screenshot and opens it in the browser.
```js
takeScreenshot(
    // this is the callback function
    function(url){
        // redirect to the data URL
        window.location.href = url;
    }
)
```

### Logs (`log-message.js`)
Only has one function:
#### `log(message)`
Prints a message to the visible logging element if it exists, and to the console otherwise.

The visible logging element can be any HTML element that displays text (`pre`, `h2`, `p` etc.) and has the ID `logMessage`. It is automatically detected.

**Argument:** `message` - the message to log.

**Example:**
Prints "Hello world!":
```js
log("Hello world!")
```

Which, if the visible logging element exists, will result in the message appearing on screen, looking something like this:
<img src="../img/log_message.png" alt="Text in a monospace font. There are 5 lines - the last 3 are 'Hello world!', 'Hiding autoplay screen' and 'Marker loaded'." width="500"/>