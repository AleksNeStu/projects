# Projects

⛱️ Just to do not forget it 😎 Some educational tips and trainings 🏖️

💻 Deep Dive Coding 🛸

[api](/api) - API stuff
   - [client](/api/client) - API clients
   - [server](/api/server) - API servers
        - [django](/api/server/django) - Django server examples
        - [fast_api](/api/server/fast_api) - FastAPI server examples
        - [flask](/api/server/flask) - Flask server examples
   - [test](/api/test) - API testsing (load, ...)

[async](/async) - Asynchronous, Multi-Threading, Multi-Processing, GIL, ...

[auto](/auto) - Automation

[cloud](/cloud) - Cloud providers and tech stack
   - [aws](/cloud/aws) - API clients
   - [azure](/cloud/azure) - API servers
   - [gcp](/cloud/gcp) - API servers

[code](/code) - Coding collections (algorithms, solutions, complexity, ...)
   - [complexity](/code/complexity) - Complexity
   - [time](/code/time) - Time
   - [validation](/code/validation) - Validation

[data](/data) - Data Engineering
   - [db](/data/db) - DB
   - [etl](/data/etl) - ETL (ELT)
     - [merge_data_app](/data/etl/001_merge_data) - Merge inconsistent data app
   - [migrations](/data/migrations) - Data (DB) migrations

[debug](/debug) - Debug, Memory

[doc](/doc) - Documentations
   - [cheats](/doc/cheats) - Cheat sheets
   - [help](/doc/help) - Help for different areas of DEV life:)
   - [interview](/doc/interview) - Interview examples 

[docker](/docker) - Docker

[frameworks](/frameworks) - Frameworks
    - [django](/frameworks/django)  - Django

[queue](/queue) - Queue
    [queues](/queue/queues) - Queues
    [brokers](/queue/brokers) - Brokers
    

[scripts](/scripts) - Scripts

[tasks](/tasks) - Tests coding tasks ...

[web_apps](/web_apps) Web applications (FE | BE or only BE) 
   - [pypi-web-app](/web_apps/001_pypi) - Demo Web App on Pyton3, Flask, SQLAlchemy, Alembic, Jinja
   - [store-wed-app](/web_apps/002_store) - Demo Web App on Pyton3, Django





# Virtual env install
```sh
dnf install python3.10 poetry

rm -rf .venv
poetry config virtualenvs.in-project true
poetry env use 3.10
source .venv/bin/activate
poetry install
poetry shell
```

# NOTES:
1) Do not use code dir as module to avoid an err during bootstrap procedures:
```
Werkzeug AttributeError: 'module' object has no attribute 'InteractiveInterpreter'
```
