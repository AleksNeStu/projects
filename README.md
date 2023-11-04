# Projects

⛱️ Just to do not forget it 😎 Some educational tips and trainings 🏖️

💻 Deep Dive Coding 🛸

[api](/api) - API solutions

- [client](/api/client) - API clients
- [openapi](/api/openapi) - Open API standard
- [server](/api/server) - API servers
- [test](/api/test) - API testsing

[apps](/apps) - Applications
- [course_mod_apps](/apps/course_mod_apps) - **`Course materials based developed apps with own deep dive
  modification 😎`**
  - [pypi-web-app](/apps/course_mod_apps/pypi_web_app) - PyPi clone (Demo Web App on Pyton3, Flask, SQLAlchemy,
    Alembic, Jinja)
- [own_apps](/apps/own_apps) - **`Own developed apps 🛸`**
  - [etl_merge_data](/apps/own_apps/etl_merge_data) - Merge inconsistent data ETL app
  - [get_youtube_info](/apps/own_apps/get_youtube_info) - Mixed mode (Wed Scrapping and API) based app to get YouTube
    chanel extended information


[async](/async) - Asynchronous, Multi-Threading, Multi-Processing solutions

[cache](/cache) - Cache solutions
- [python_cache](/cache/python_cache) - Python cache

[cloud](/cloud) - Cloud solutions
- [aws](/cloud/aws) - AWS
- [azure](/cloud/azure) - Azure
- [gcp](/cloud/gcp) - GCP

[code](/code) - Code solutions
- [complexity](/code/complexity) - Complexity
- [validation](/code/validation) - Validation
- [debug](/code/debug) - Debug, Memory

[common](/common) - **`Common code based for rest of the sub-projects`**

[code_tasks](/tasks) - Coding tasks solutions

[data](/data) - Data Engineering solutions
- [db](/data/db) - DB
- [etl](/data/etl) - ETL (ELT)
- [migrations](/data/migrations) - Data, Schema, DB migrations

[doc](/doc) - Documentation

- [cheats](/doc/cheats) - Cheat sheets
- [help](/doc/help) - Help for different areas of DEV life:)
- [interview](/doc/interview) - Interview examples

[docker](/docker) - Docker solutions

[frameworks](/frameworks) - Frameworks

- [django](/frameworks/django)  - Django
- [fastapi](/frameworks/fastapi)  - Fast Api
- [flask](/frameworks/flask)  - Flask

[queue](/queue) - Queue solutions
- [brokers](/queue/brokers) - Brokers
- [queues](/queue/queues) - Queues

[scripts](/scripts) - Scripts
- [auto](/scripts/auto) - Automation solutions
- [helpers](/scripts/helpers) - Helpers
- [python](/scripts/python) - Python based solutions and examples
- [sh](/scripts/sh) - SH based solutions and examples

### Project run locally
```sh
chmod +x ./setup.sh && bash ./setup.sh
```

### Notes

- Do not use `code` dir as module (with `__init__.py`) to avoid an error raising during bootstrap procedures.
```
Werkzeug AttributeError: 'module' object has no attribute 'InteractiveInterpreter'
```
