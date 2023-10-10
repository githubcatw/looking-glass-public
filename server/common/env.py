
import os

"""
Gets an environment variable and closes the program if it doesn't exist.
"""
def get_env_or_exit(name):
    # Get the variable if possible
    var = os.environ.get(name, None)
    # If it doesn't exist, print a warning and exit
    if var == None:
        print(f"Looking Glass can't work without the environment variable {name} being set.")
        print("Please set this variable and restart the Looking Glass server.")
        exit()
    # Otherwise, return the variable
    return var