# Projects

⛱️ Just to do not forget it 😎 Some educational tips and trainings 🏖️

💻 Deep Dive Coding 🛸

[.tmpl]

[api](/api) - API stuff
   - [client](/api/client) - API clients
   - [server](/api/server) - API servers
- [openapi](/api/openapi) - Open API
- [test](/api/test) - API testsing

[async](/async) - Asynchronous, Multi-Threading, Multi-Processing, GIL, ...

[auto](/auto) - Automation

[cache](/cache) - Cache

[cloud](/cloud) - Cloud providers and tech stack
   - [aws](/cloud/aws) - API clients
   - [azure](/cloud/azure) - API servers
   - [gcp](/cloud/gcp) - API servers

[code](/code) - Coding collections (algorithms, solutions, complexity, ...)
   - [complexity](/code/001_complexity) - Complexity
   - [time](/code/time) - Time
   - [validation](/code/002_validation) - Validation

[code_tasks](/tasks) - Tests coding tasks ...

[data](/data) - Data Engineering

- [db](/data/001_db) - DB
- [etl](/data/002_etl) - ETL (ELT)
     - [merge_data_app](/data/002_etl/001_merge_data) - Merge inconsistent data app
- [migrations](/data/003_migrations) - Data (DB) migrations

[debug](/debug) - Debug, Memory

[doc](/doc) - Documentations
   - [cheats](/doc/cheats) - Cheat sheets
   - [help](/doc/help) - Help for different areas of DEV life:)
   - [interview](/doc/interview) - Interview examples 

[docker](/docker) - Docker

[frameworks](/frameworks) - Frameworks
   - [django](/frameworks/django)  - Django

[queue](/queue) - Queue
   - [queues](/queue/queues) - Queues
   - [brokers](/queue/brokers) - Brokers

[scripts](/scripts) - Scripts
   - [helpers](/scripts/helpers) - Helpers
      -  [get_youtube_urls](/scripts/helpers/001_get_youtube_urls) - Helper which use Self and Public YouTube Scrapers as wel las Api wrappers to get YouTube data (channel, playlists, find diff between main channel and playlists, etc. Make possibility to mix behaviour and download videos.)
          

[web_apps](/web_apps) Web applications (FE | BE or only BE) 
   - [pypi-web-app](/web_apps/001_pypi) - Demo Web App on Pyton3, Flask, SQLAlchemy, Alembic, Jinja
   - [store-wed-app](/web_apps/002_store) - Demo Web App on Pyton3, Django





# Virtual env install
```sh
export PROJECT_DIR="/home/..."; export POETRY_VERSION=1.6.1; export PYTHON_VERSION=3.12
sudo dnf install python$PYTHON_VERSION poetry
sudo dnf install python$PYTHON_VERSION-devel.x86_64  # for Cython compilation for IDE
curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -

cd $PROJECT_DIR
rm -rf .venv
poetry config virtualenvs.in-project true
poetry env use $PYTHON_VERSION
source .venv/bin/activate
poetry install
poetry shell
```

# NOTES:
1) Do not use code dir as module to avoid an err during bootstrap procedures:
```
Werkzeug AttributeError: 'module' object has no attribute 'InteractiveInterpreter'
```
