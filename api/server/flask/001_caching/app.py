import logging
import sys

import dotenv
import requests
from codetiming import Timer
from flask import Flask, request, jsonify
from flask_caching import Cache
from humanfriendly import format_timespan

# ENV
dotenv.load_dotenv("./app.env") # to project os.getenv('***')
env = dotenv.dotenv_values("./app.env") # to var

# Logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = Flask(__name__)
app.config.from_mapping(**env)

cache = Cache(app)


@app.route("/universities/")
@cache.cached(timeout=777, query_string=True)
# query_string — Default False. When True, the cache key used will be the result of hashing the ordered query string parameters. This avoids creating different caches for the same query just because the parameters were passed in a different order.
def get_universities():
    # http://universities.hipolabs.com
    # {"example": "http://universities.hipolabs.com/search?name=middle&country=Turkey", "author": {"name": "hipo", "website": "http://hipolabs.com"}, "github": "https://github.com/Hipo/university-domains-list"}

    # http://universities.hipolabs.com/search?name=middle
    # http://universities.hipolabs.com/search?name=middle&country=turkey
    # http://universities.hipolabs.com/search?country=United States&name=Mart

    country = request.args.get('country', '')
    API_URL = f"http://universities.hipolabs.com/search?country={country}"

    with Timer(name=f'{__file__}',
               text=lambda secs: f"Get universities request time: {format_timespan(secs)}",
               logger=logging.info):
        resp = requests.get(API_URL)

    return jsonify(resp.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)