# Copyright 2015 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import socket

from flask import Flask, request


app = Flask(__name__)


def is_ipv6(addr):
    """Checks if a given address is an IPv6 address.

    Args:
        addr: An IP address object.

    Returns:
        True if addr is an IPv6 address, or False otherwise.
    """
    try:
        socket.inet_pton(socket.AF_INET6, addr)
        return True
    except OSError:
        return False


# [START example]
@app.route("/")
def index():
    """Serves the content of a file that was stored on disk.

    The instance's external address is first stored on the disk as a tmp
    file, and subsequently read. That value is then formatted and served
    on the endpoint.

    Returns:
        A formatted string with the GAE instance ID and the content of the
        seen.txt file.
    """
    instance_id = os.environ.get("GAE_INSTANCE", "1")

    user_ip = request.remote_addr

    # Keep only the first two octets of the IP address.
    if is_ipv6(user_ip):
        user_ip = ":".join(user_ip.split(":")[:2])
    else:
        user_ip = ".".join(user_ip.split(".")[:2])

    with open("/tmp/seen.txt", "a") as f:
        f.write(f"{user_ip}\n")

    with open("/tmp/seen.txt") as f:
        seen = f.read()

    output = f"Instance: {instance_id}\nSeen:{seen}"
    return output, 200, {"Content-Type": "text/plain; charset=utf-8"}


# [END example]


@app.errorhandler(500)
def server_error(e):
    """Serves a formatted message on-error.

    Returns:
        The error message and a code 500 status.
    """
    logging.exception("An error occurred during a request.")
    return (
        f"An internal error occurred: <pre>{e}</pre><br>See logs for full stacktrace.",
        500,
    )


if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
