#set -x

cd ../pypi_org
pwd
set -o allexport && source ../configs/local.env && source ../configs/flask.env && set +o allexport

source ../.venv/bin/activate
python3 bin/insert_data.py

#set +x