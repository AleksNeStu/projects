import os
import sys

import dotenv
import flask
import requests
from celery import Celery, current_app
from celery.bin import worker
from flask import render_template, request, redirect, url_for


module_name = os.path.basename(sys.modules[__name__].__file__).split(".")[0]

# add_module_to_sys_path
directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, directory)

url_txt = os.path.join(directory, "url.txt")

dotenv.load_dotenv("./app.env")
env = dotenv.dotenv_values("./app.env")


flask_app = flask.Flask(module_name)
flask_app.config.from_mapping(**env)


def inst_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config.get("CELERY_BACKEND_URL", ""),
        broker=app.config.get("CELERY_BROKER_URL", ""),
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery_app = inst_celery(flask_app)

@celery_app.task()
def get_dog_pics(breed_type, limit):
    url = f"https://dog.ceo/api/breed/{breed_type}/images/random/{limit}"
    r = requests.get(url)
    files = r.json()
    # files = flask.jsonify()

    for file in files["message"]:
        with open(url_txt, "a") as myfile:
            myfile.write(" " + file)

    return files["message"]

@flask_app.route("/", methods=["GET", "POST"])
def index():
    # we define dog breeds so the user chooses from this list
    dog_breeds = [
        "affenpinscher",
        "dalmatian",
        "germanshepherd",
        "kelpie",
        "labrador",
        "husky",
        "otterhound",
        "pitbull",
        "pug",
        "rottweiler",
    ]

    # we store links in this list
    pictures = []

    f_urls = open(url_txt, "r")

    for images in f_urls:
        image = images.replace(",", " ")
        image = image.replace('"', "")
        pictures.extend(image.split())

    # on form submission, the task is ran
    if request.method == "POST":
        if request.form["submit"] == "getDogPics":
            breed_type = request.form.get("breed")
            limit = request.form.get("limit")
            get_dog_pics.delay(breed_type, limit)
            return redirect(url_for("index"))

        # an option for clearing all the links
        elif request.form["submit"] == "clearDogPics":
            f = open(url_txt, "w")
            f.close()
            return redirect(url_for("index"))

    # Results
    return render_template("template.html", breeds=dog_breeds, link=pictures)

# if __name__ == "__main__":
#     pass
#     # 1) Flask
#     # flask_app.run(host='0.0.0.0', port=5000, debug=True)
#
#     # 2) Celery
#     # a)
#     # argv = [
#     #     'worker',
#     #     '--loglevel=DEBUG',
#     # ]
#     # celery_app.worker_main(argv)
#
#     # b)
#     # app = current_app._get_current_object()
#     # worker = worker.worker(app=celery_app)
#     # options = {
#     #     'loglevel': 'INFO',
#     #     'traceback': True,
#     # }
#     # worker.run(**options)


# LOG
#  -------------- celery@he v5.2.7 (dawn-chorus)
# --- ***** -----
# -- ******* ---- Linux-6.0.10-300.fc37.x86_64-x86_64-with-glibc2.34 2022-12-01 01:16:31
# - *** --- * ---
# - ** ---------- [config]
# - ** ---------- .> app:         app:0x7fd2c65e55e0
# - ** ---------- .> transport:   amqp://root:**@localhost:5672/vhost
# - ** ---------- .> results:     sqlite:///app.db
# - *** --- * --- .> concurrency: 8 (prefork)
# -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
# --- ***** -----
#  -------------- [queues]
#                 .> celery           exchange=celery(direct) key=celery
#
#
# [tasks]
#   . app.get_dog_pics
#
# [2022-12-01 01:16:31,870: INFO/MainProcess] Connected to amqp://root:**@127.0.0.1:5672/vhost
# [2022-12-01 01:16:31,872: INFO/MainProcess] mingle: searching for neighbors
# [2022-12-01 01:16:32,888: INFO/MainProcess] mingle: all alone
# [2022-12-01 01:16:32,894: INFO/MainProcess] celery@he ready.