from flask import Blueprint, request, make_response
import json
import re
import requests

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

api = Blueprint('api', __name__)

cache = dict()

@api.route("/get_playlist")
def get_playlist():
    url = request.args["url"]
    if url in cache:
        return cache[url]
    html = getHTML(url)
    id = extractid(html)
    rss = getHTML("https://www.youtube.com/feeds/videos.xml?channel_id=" + id)
    latest_vid = extractvid(rss)
    response_data = {"url": "https://www.youtube.com/watch?v=" + latest_vid + "&list=UU" + id[2:]}
    response = make_response(json.dumps(response_data))
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')  # Allow the Content-Type header
    response.headers.add('Access-Control-Allow-Methods', 'GET')  # Allow GET requests
    cache[url] = response
    return response
