from flask import Flask, render_template

app = Flask(__name__)

from youtube_helper.api import api
app.register_blueprint(api, url_prefix="/api")
