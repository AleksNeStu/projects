#set -x

cd ../pypi_org
pwd
set -o allexport && source ../configs/local.env && source ../configs/flask.env && set +o allexport
source ../.venv/bin/activate
#flask run --port=5000 --without-threads

IS_DEPLOY='1' && python3  app.py run --port=5000 --host=0.0.0.0 --without-threads

# env FLASK_APP=app.py flask run
#set +x