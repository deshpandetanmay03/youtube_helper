from flask import Flask, render_template

app = Flask(__name__)

from youtube_helper.home import home
app.register_blueprint(home, url_prefix="/")

from youtube_helper.api import api
app.register_blueprint(api, url_prefix="/api")

from youtube_helper.playlist import playlist
app.register_blueprint(playlist, url_prefix="/playlist")
