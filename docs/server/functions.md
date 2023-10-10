# Backend functions
![Banner image](../../img/banners/server-structure.png)
This document is documentation for all functions in the Looking Glass backend, including the main source code and all custom libraries.

## `common`
This module contains functions that are used in all

### `image_decoder`
Contains functions for decoding Base64 encoded images.

#### `decode_data_url`
Decodes the image from a given `data:` url.

**Arguments:**
| Name         | Meaning              |
|--------------|----------------------|
| `url`        | the URL to decode    |

**Returns:** the image as a byte array.

**Raises:** `ValueError` - if the URL isn't a data: URL.

#### `decode_data_url_to_file`
Decodes the data from the passed `data:` URL and saves it to a file.

**Arguments:**
| Name         | Meaning                      |
|--------------|------------------------------|
| `url`        | the URL to decode            |
| `path`       | the path to save the file to |

**Returns:** nothing.

**Raises:** `ValueError` - if the URL isn't a data: URL.

### `tg_init_data`
Contains functions for verifying and decoding Telegram Mini App init data.

#### `parse_query_string`
Parses a query string and returns its contents as a dictionary.

**Arguments:**
| Name         | Meaning                    |
|--------------|----------------------------|
| `string`     | the query string to decode |

**Returns:** the query string as a dict.

#### `is_init_data_valid`
Checks if mini app initialization data is valid.

**Arguments:**
| Name    | Meaning                                                                 |
|---------|-------------------------------------------------------------------------|
| `data`  | the data as a dictionary (use `parse_query_string` to convert it to one). |
| `token` | the token of the bot this data is coming from.                          |

**Returns:** True if the data is coming from Telegram, otherwise False.

#### `load_init_data`
Loads mini app initialization data.

**Arguments:**
| Name    | Meaning                                        |
|---------|------------------------------------------------|
| `data`  | the data.                                      |
| `token` | the token of the bot this data is coming from. |

**Returns:** if the data is valid, a dictionary version of it.

**Raises:** `ValueError` - if the initialization data is invalid.

### `env`
Has just one convenience function:

#### `get_env_or_exit`
Gets an environment variable and closes the program if it doesn't exist.

**Arguments:**
| Name    | Meaning              |
|---------|----------------------|
| `name`  | the variable's name. |

**Returns:** the variable's value.