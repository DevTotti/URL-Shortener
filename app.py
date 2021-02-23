from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
import string, random
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGO_URI"]
mongo = PyMongo(app)

url_db = mongo.db.mainurl


def generate_encode():
    text = [''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(6)])]
    random.shuffle(text)
    sub_url = ''.join(text)
    return sub_url



@app.route("/", methods=["POST"])
def shorten_url():
    host = request.host_url
    print(host)
    url_ = request.get_json()['url']
    print(url_)
    original_url = str.encode(url_)
    if urlparse(original_url).scheme == '':
        original_url = "http://"+original_url
    
    else:
        original_url = original_url

    encoded_path = ''

    exist = True

    while exist:
        url_path = generate_encode()
        print(url_path)
        response = url_db.find_one({'encoded':url_path})
        if response:
            exist = True
        else:
            encoded_path = url_path
            exist = False

    url_data = url_db.insert({
        "encoded": encoded_path,
        "original_url": original_url
    })

    encoded_url = host + encoded_path
    return encoded_url



@app.route("/<short_url>")
def request_url(short_url):
    host = request.host_url
    url = host

    try:

        response = url_db.find_one({ "encoded": short_url })
        original_url = response["original_url"]
        return redirect(original_url)

    except Exception as e:
        print(str(e))
        return redirect(host)

           


if __name__ == "__main__":
    app.run(debug=True, port=4500)

