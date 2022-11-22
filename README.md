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

[async](/async) - Asynchronous, Multi-Threading, Multi-Processing

[cloud](/cloud) - Cloud providers and tech stack

[code](/code) - Coding collections (algorithms, solutions, complexity, ...)

[data](/data) - Data Engineering
   - [etl](/data/etl) - ETL (ELT)
        - [*merge_data](/data/etl/001_merge_data) - Application to merge inconsistent input data from input and convert it

        - [migrations](/data/migrations) - Data (DB) migrations
          - [alembic_quickstart](/data/migrations/001_alembic_quickstart) - Alembic quickstart migrations

[debug](/debug) - Debug
   - [memory-leaks](/memory-leaks) - Memory leaks examples

[doc](/doc) - Documentations
   - [cheats](/doc/cheats) - Cheat sheets
   - [help](/doc/help) - Help for different areas of DEV life:)
   - [interview](/doc/interview) - Interview examples 

[frameworks](/frameworks) - Frameworks
    - [django](/frameworks)

[scripts](/scripts) - Scripts

[web_apps](/web_apps) Web applications (FE | BE or only BE) 
   - [pypi-web-app](/web_apps/001_pypi) - Demo Web App on Pyton3, Flask, SQLAlchemy, Alembic, Jinja
   - [store-wed-app](/web_apps/002_store) - Demo Web App on Pyton3, Django

[tasks](/tasks) - Tests coding tasks and more



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
