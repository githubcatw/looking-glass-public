import base64

"""
Decodes the data from the passed 'data:' URL.
"""
def decode_data_url(url):
    # If the URL doesn't start with "data:" and doesn't use the base64 encoding, it's not supported.
    if not url.startswith("data:") and not "base64," in url:
        # Raise an error, so functions that use this function can catch it and react to it.
        raise ValueError("This URL isn't supported.")

    # Get only the data part - it comes after "base64,".
    data = url.split("base64,")[1]
    # Return the decoded data.
    return base64.b64decode(data)

"""
Decodes the data from the passed 'data:' URL and saves it to a file.
"""
def decode_data_url_to_file(url, path):
    # Decode the data using the function above.
    data = decode_data_url(url)
    # Write it to the path.
    with open(path, 'wb') as out:
        out.write(content)