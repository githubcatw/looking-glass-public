"""
Looking Glass - server
API initialization
(c) 2023 githubcatw
"""

# Import flask
from flask import Flask

# Import uvicorn (web server) and async extensions for Flask
import uvicorn
from asgiref.wsgi import WsgiToAsgi

# Get the port number from the config
from .. import PORT

# Import all blueprints
from .bot_endpoints import flask_app as bot_bp
from .post import flask_app as post_bp

# Create a Flask app
app = Flask(__name__)
# Register all blueprints
app.register_blueprint(bot_bp)
app.register_blueprint(post_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World! :3</p>"

"""
Starts the API server.
"""
def start():
    # Runs the app and makes it visible to everyone
    app.run(host="0.0.0.0")

"""
Creates a web server for the Flask app.
"""
def create_ws():
    return uvicorn.Server(
        config=uvicorn.Config(
            app=WsgiToAsgi(app),
            port=int(PORT),
            use_colors=False,
            host="0.0.0.0",
        )
    )

def get_app():
    return WsgiToAsgi(app)