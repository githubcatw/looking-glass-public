# Used for validation.
import hashlib
import hmac
# Used to parse the initialization data.
import urllib.parse
# Used to convert parts of the initialization data.
import json

"""
Parses a query string and returns its contents as a dictionary.
"""
def parse_query_string(string):
    # Use urllib to parse it.
    parse = urllib.parse.parse_qsl(string)
    # Return the result as a dictionary.
    return dict(parse)


"""
Checks if mini app initialization data is valid.

Arguments:
- data - the data as a dictionary (use parse_query_string to convert it to one).
- token - the token of the bot this data is coming from.

Returns:
True if the data is coming from Telegram, otherwise False.
"""
def is_init_data_valid(data, token):
    # Generate a check string
    check_string = ""
    # Sort the dictionary keys alphabetically
    sortedkeys = sorted(data, key=str.lower)
    # For all of the sorted keys:
    for key in sortedkeys:
        # Skip the hash
        if key != "hash":
            # Add the key and its value to the check string in Telegram's required format
            check_string += key + "=" + data[key] + "\n"
    
    # Remove the last character (an extra "\n") from the check string
    # ([:-1] means "from the start to the second to last character")
    check_string = check_string[:-1]

    # Sign the bot token with the key "WebAppData" - this is the check string encryption key
    check_enc_key = hmac.new(b"WebAppData", msg=bytes(token, "utf-8"), digestmod=hashlib.sha256)
    # Encrypt the check string with that key (both as bytes)
    check_hash = hmac.new(check_enc_key.digest(), msg=bytes(check_string, "utf-8"), digestmod=hashlib.sha256)
    print("got " + check_hash.hexdigest())
    # If it matches the hash provided in the initialization data, it's valid.
    # hmac.compare_digest is used since it's supposedly more secure.
    print("should be " + data["hash"])
    return hmac.compare_digest(check_hash.hexdigest(), data["hash"])

"""
Loads mini app initialization data.

Arguments:
- data - the data.
- token - the token of the bot this data is coming from.

Returns:
if the data is valid, a dictionary version of it.

Raises:
ValueError - if the initialization data is invalid.
"""
def load_init_data(data, token):
    # Parse the init data.
    init_data = parse_query_string(data)
    # Raise an error if it's invalid.
    if not is_init_data_valid(init_data, token):
        raise ValueError("Initialization data is invalid.")
    
    # Do some processing to make it easier to work with.

    # Telegram sends some fields as JSON; convert them to Python dictionaries
    if "user" in init_data:
        init_data["user"] = json.loads(init_data["user"])
    if "receiver" in init_data:
        init_data["receiver"] = json.loads(init_data["receiver"])
    if "chat" in init_data:
        init_data["chat"] = json.loads(init_data["chat"])

    # Return the init data.
    return init_data

