set -x

set -o allexport && source configs/local.env && set +o allexport

source .venv/bin/activate
python3 pypi_org/bin/insert_data.py

set +x