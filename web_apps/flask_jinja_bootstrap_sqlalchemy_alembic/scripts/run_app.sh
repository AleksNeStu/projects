set -o allexport && source configs/local.env && set +o allexport \
&& flask run --port=5000 --without-threads

# python app.py

# env FLASK_APP=app.py flask run