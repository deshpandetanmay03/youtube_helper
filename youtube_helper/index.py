from flask import Flask, render_template, request, make_response
import requests
import re
import json

def getHTML(url):
    response = requests.get(url)
    htmlText = response.text
    return htmlText

def extractid(str):
    pattern = r'vnd.youtube://www.youtube.com/channel/(.*?)"'
    match = re.search(pattern, str)[1]
    return match if match else None

def extractvid(str):
    pattern = r'<id>yt:video:(.*?)</id>'
    match = re.search(pattern, str)
    return match.group(1) if match else None

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/channelplaylist")
def channelplaylist():
    return render_template("channelplaylist.html")

@app.route("/get_playlist")
def get_playlist():
    url = request.args["url"]
    html = getHTML(url)
    id = extractid(html)
    rss = getHTML("https://www.youtube.com/feeds/videos.xml?channel_id=" + id)
    latest_vid = extractvid(rss)
    response_data = {"url": "https://www.youtube.com/watch?v=" + latest_vid + "&list=UU" + id[2:]}
    response = make_response(json.dumps(response_data))
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')  # Allow the Content-Type header
    response.headers.add('Access-Control-Allow-Methods', 'GET')  # Allow GET requests
    return response
