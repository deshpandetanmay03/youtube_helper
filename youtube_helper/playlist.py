from flask import Blueprint, render_template

playlist = Blueprint("playlist", __name__)

@playlist.route("/channelplaylist")
def channelplaylist():
    return render_template("channelplaylist.html")
