from collections import defaultdict
from datetime import timedelta, datetime
from typing import List

import requests
from flask import Flask, jsonify

posts_url = "https://jsonplaceholder.typicode.com/posts"
comments_url = "https://jsonplaceholder.typicode.com/comments"

app = Flask(__name__)

cache_timeout = timedelta(seconds=20)  # Define the cache timeout period (e.g., 20 seconds)
_timestamp = None
_post_id_full_data = {}  # Initialize the post-comment map dictionary


def get_post_id_comments_data(comments_data: List[dict]):
    post_id_comments_data = defaultdict(list)
    for comment_data in comments_data:
        c_post_id = comment_data['postId']
        post_id_comments_data[c_post_id].append(comment_data)

    return post_id_comments_data

def get_post_id_full_data(posts_data: List[dict], post_id_comments_data: dict):
    post_id_full_data= {}
    for post_data in posts_data:
        p_post_id = post_data["id"]
        post_comments = post_id_comments_data.get(p_post_id)
        if post_comments:
            # post_data.update({"comments": post_comments, 'timestamp': datetime.now()})
            post_data.update({"comments": post_comments})
        post_id_full_data[p_post_id] = post_data

    assert len(posts_data) == len(post_id_full_data)

    # post_id_full_data["_timestamp"] = datetime.now()
    return post_id_full_data

def is_cache_expaired():
    global _timestamp
    res = bool((datetime.now() - _timestamp) > cache_timeout)
    return res

@app.route('/get_posts_comments', methods=['GET'])
def get_posts_comments():
    global _post_id_full_data, _timestamp
    if _post_id_full_data and _timestamp and is_cache_expaired():
        _post_id_full_data.clear()

    if not _post_id_full_data:  # If the map is empty, fetch data from the API
        posts_response = requests.get(posts_url)
        comments_response = requests.get(comments_url)

        if posts_response.status_code == 200 and comments_response.status_code == 200:
            posts_data = posts_response.json()
            comments_data = comments_response.json()

            post_id_comments_data = get_post_id_comments_data(comments_data)
            _post_id_full_data = get_post_id_full_data(posts_data, post_id_comments_data)
            _timestamp = datetime.now()

    return jsonify(_post_id_full_data)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()