# Creating your own content
This requires some edits to the Looking Glass app's code.

## Creating a marker
First, you have to create a [marker](terminology.md#Marker). Looking Glass will track it and show your AR content on it.

1. Make the image that will be used as the marker. This could be any photo or illustration. Images with more detail (like photos) result in better tracking quality than ones with less detail (like minimalist art).
2. Go to the [NFT Marker Creator](https://carnaux.github.io/NFT-Marker-Creator/) site. This tool is used to convert images into a format that Looking Glass can recognize.
3. Drag your image into the "Click or drag image" box.
4. Click "Generate" and wait for a while until the marker files are generated.
    > Note: your browser might show a "page unresponsive" warning at this step - it's normal, wait until the files are generated and don't close the page.
5. Once it's done you should have 3 files with the same name as the image - these are the marker files used by Looking Glass.

## Creating the contents
This is what will be shown to users when the marker is detected.

OBJ and gLTF (.glb) 3D models are supported. Most commercial and open-source 3D modelling apps support exporting to at least one of these formats, and there are a lot of pre-made 3D models available on the internet.

## Putting it all together
Finally, you have to tell the app where to find the marker and what content to show.

1. Upload the marker files to the server that hosts the Looking Glass app. They can be placed anywhere, but we recommend making a folder in the `markers` folder.
2. Upload the model to the server. It can be placed anywhere too, but we recommend using the `models` folder.
3. Open the `index.html` file in a text editor.
4. Add an `a-nft` to the `a-scene` with a link to your marker files. As the URL set the path of your markers without the extension.
    - For example, if your marker files are at `/app/markers/kitten` and are named `kitten.fset3`, `kitten.fset` and `kitten.iset`, the URL is `./app/markers/kitten/kitten`.
    - Code example:
    ```html
    <a-scene>
        <!-- ... -->
        <a-nft
            type="nft"
            url="(marker URL)"
            smooth="true"
            smoothCount="10"
            smoothTolerance=".01"
            smoothThreshold="5"
        >
    ```
5. Add an `a-entity` to your `a-scene`. As the `url` set the path to your model.
    - Code example:
    ```html
    <a-scene>
        <!-- ... -->
        <a-nft>
            <!-- ... -->
            <a-entity
                gltf-model="(model URL)"
                scale="100 100 100"></a-entity>
        </a-nft>
    </a-scene>
    ```
6. Run the app. You might need to resize, rotate or move the object, which is done using the `scale`, `rotation` and `transform` attributes respectively.

---

[back to setup guide](setup.md) | [back to documentation list](../README.md)