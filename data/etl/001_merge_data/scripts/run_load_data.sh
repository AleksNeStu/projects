#set -x
source /Projects/projects/.venv/bin/activate

cd ../merge_app
pwd
#set -o allexport && source ../configs/local.env && source ../configs/flask.env && set +o allexport

python3 bin/load_data.py

#set +x