#set -x

cd ../pypi_org
pwd
set -o allexport && source ../configs/local.env && source ../configs/flask.env && set +o allexportsource ../.venv/bin/activatepytest ../tests/src --disable-warnings

#set +x
