import requests
from codetiming import Timer
from flask import Flask, request, jsonify
from humanfriendly import format_timespan
import logging


app = Flask(__name__)


@app.route("/universities/")
def get_universities():
    # http://universities.hipolabs.com
    # {"example": "http://universities.hipolabs.com/search?name=middle&country=Turkey", "author": {"name": "hipo", "website": "http://hipolabs.com"}, "github": "https://github.com/Hipo/university-domains-list"}

    # http://universities.hipolabs.com/search?name=middle
    # http://universities.hipolabs.com/search?name=middle&country=turkey
    # http://universities.hipolabs.com/search?country=United States&name=Mart

    country = request.args.get('country', '')
    API_URL = f"http://universities.hipolabs.com/search?country={country}"

    with Timer(name=f'{__file__}',
               text=lambda secs: f"Elapsed time: {format_timespan(secs)}",
               logger=logging.info):
        resp = requests.get(API_URL)

    return jsonify(resp.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)