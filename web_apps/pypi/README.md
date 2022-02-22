# Demo Web App on Pyton3, Flask, SQLAlchemy, Alembic, Jinja

**Python 3 / Poetry / Flask (Flask Extensions) / Werkzeug / Jinja (CSS, HTML, Cookies, auth) / Bootstrap / SQLAlchemy / Alembic / SQLite / MongoDB / Pytest / Docker / Linux / NGINX/ uWSGI / IntelliJ** \
*replica of https://pypi.org/*

## Setup

**Using container version of application**
https://hub.docker.com/r/nestu/pypi_demo/tags

a) OS without run of app :
**core**:`docker pull nestu/pypi_demo:core`
```sh
# from host
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
sudo docker exec –it os zsh
```

b) OS with run flask app:

**flask**:`docker pull nestu/pypi_demo:flask`
```sh
# from host
docker-compose -f docker-compose.flask.yml build
docker-compose -f docker-compose.flask.yml up
sudo docker exec –it os zsh
# from container
httpp 127.0.0.1:5000

# from host:
# http://localhost:8080/
```

c) Python with run uwsgi app (using nginx):
**uwsgi**`docker pull nestu/pypi_demo:uwsgi`
```sh
# from host
docker-compose -f docker-compose-uwsgi.yml build
docker-compose -f docker-compose-uwsgi.yml up
sudo docker exec –it app zsh
# from container
httpp 127.0.0.1:80

# from host:
# http://localhost:8080/
```

**NOTES:**
- Dirs desc:
docker `/tmp/pypi` -> host `projects/web_apps/pypi`
docker `/tmp/pypi_docker` -> `projects/web_apps/pypi_docker` - not git dir (
   for docker app code on gly changes)
docker `pypi` -> docker `/tmp/pypi_docker` - symlink

**Using local version of application**

1) Clone the app project.
3) Install requirements using poetry. 2.1) Python

```shell
cd web_apps/pypi
poetry config virtualenvs.in-project true
poetry shell
poetry install
```

or to just install the added package(s) (and remove any dev packages that were
already installed if you killed it too late):

```
poetry install --no-dev
```

[Creating a Flask Project](https://www.jetbrains.com/help/pycharm/creating-flask-project.html)

2.2) JS

```shell
cd web_apps/pypi
npm i or npm ci
npm install --save-dev
```

To use local css and js of bootstrap /pypi_org/templates/shared/_layout.html

```shell
cd web_apps/pypi/pypi_org
ln -s ../node_modules
```

```html

<link rel="stylesheet"
      href="/node_modules/bootstrap/dist/css/bootstrap.css">
```

3) Run app:

3.1) Setup IDE project structure
<p align="center">
<img src="assets/pr-1.png" alt="Project Settings / Project" width="70%">
<img src="assets/pr-2.png" alt="Project Settings / Modules tree" width="70%">
<img src="assets/pr-3.png" alt="Project Settings / Modules env" width="70%">
<img src="assets/pr-4.png" alt="Project Settings / Modules tree" width="70%">
<img src="assets/pr-5.png" alt="Project Settings / Modules env" width="70%">
<img src="assets/pr-6.png" alt="Platform Settings / SDKs" width="70%">
</p>

3.2) Run app via command interface:
`cd <project_dir>`
`scripts/run_app.sh`

3.3) Run app via IDE in debug mode:

**NOTE:**
Need plugin for IDE:
[EnvFile](https://plugins.jetbrains.com/plugin/7861-envfile)
<p align="center">
<img src="assets/ide-1.png" alt="EnvFile plugin for IDE" width="70%">
</p>

a) Flask module
<p align="center">
<img src="assets/ide-2.png" alt="Flask module" width="70%">
</p>

b) Python script app.py
<p align="center">
<img src="assets/ide-3.png" alt="Python script" width="70%">
</p>

c) Flask framework \
[Run/Debug Configuration: Flask Server](https://www.jetbrains.com/help/pycharm/run-debug-configuration-flask-server.html)

<p align="center">
<img src="assets/ide-4.png" alt="Flask framework" width="70%">
</p>

4) Run scripts:

```sh
cd projects/web_apps/pypi
./scripts/run_app.sh
./scripts/run_data_insert.sh
...
```

5) DB

```sh
sudo yum install python3-devel mysql-devel
```

6) Alembic:

```sh
cd web_apps/pypi/
alembic init migrations/alembic
sudo dnf install -y python3-alembic
alembic current
# make model changes
# https://alembic.sqlalchemy.org/en/latest/autogenerate.html
alembic revision --autogenerate -m "Added last_updated column to Package cls"
# manual
alembic revision -m "new migration"

alembic upgrade head
alembic downgrade base
```

Alternative for `alembic upgrade head`:

```Python
# or https://alembic.sqlalchemy.org/en/latest/api/commands.html
from alembic.config import Config
from alembic import command

alembic_cfg = Config("/pypi_org/alembic.ini")
command.upgrade(alembic_cfg, "head")
```

7) Run app inside of docker container:
   7.1) Install docker:

```sh
# a) https://docs.docker.com/engine/install/
# e.g. https://docs.docker.com/engine/install/fedora/
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io

# b) https://docs.docker.com/engine/install/linux-postinstall/
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
# if err `connect EACCES /var/run/docker.sock`
sudo chmod o+rw /var/run/docker.sock

sudo systemctl start docker.service
sudo netstat -lntp | grep dockerd
```

7.2) Install docker-compose:

```sh
# https://docs.docker.com/compose/install/
# https://developer.fedoraproject.org/tools/docker/compose.html
# https://computingforgeeks.com/install-and-use-docker-compose-on-fedora/
```

7.3) Enable Command-line completion for docker:

```sh
#https://docs.docker.com/compose/completion/
# With oh-my-zsh shell
kate ~/.zshrc
# add to plugins=(... docker docker-compose)
source ~/.zshrc
```

7.4) Install GUI-For-Docker:

```sh
# https://appfleet.com/blog/top-gui-for-docker/
# e.g. https://dockstation.io/
# or use IDE plugins
# or https://github.com/jesseduffield/lazydocker#usage
```

7.5) Dockerfile or Docker Compose desc:
_Use long term support Ubuntu image: https://wiki.ubuntu.com/Releases_

**Dockerfile**

```yml
# https://runnable.com/docker/python/dockerize-your-flask-application
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# https://runnable.com/docker/python/dockerize-your-flask-application
# https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04#step-2-setting-up-docker
```

**Docker compose**

```sh
# https://runnable.com/docker/python/docker-compose-with-flask-apps
# https://docs.docker.com/compose/gettingstarted/
# https://www.tutorialworks.com/why-containers-stop/#what-if-my-docker-container-dies-immediately
tty=True
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
# to use increments
docker-compose -f docker-compose-new.yml build
docker-compose -f docker-compose-new.yml build --no-cache
docker-compose -f docker-compose-new.yml up
```

7.6) Connect to docker:

```sh
# https://phoenixnap.com/kb/how-to-ssh-into-docker-container
sudo docker exec –it os zsh
sudo docker attach os
```

7.7) Push / pull docker image:

```sh
docker logout
docker login --username=yourhubusername --email=youremail@company.com
docker images

# docker-compose.yml
docker image tag pypi_os:latest nestu/pypi_demo:os
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
nestu/pypi_demo   core      54f70da6fd51   15 minutes ago   968MB

docker image push nestu/pypi_demo:os

docker run --rm nestu/pypi_demo:os
docker pull nestu/pypi_demo:os
```

7.8) Non root user:
https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host
https://stackoverflow.com/questions/27701930/how-to-add-users-to-docker-container

7.9) Restart policy:
```
docker update --restart=no ba758b878e7c
```

## Tips

1) Show project structure: \
   `tree -I .env`
2) Export requirements: \
   `poetry export -f requirements.txt --output requirements.txt --without-hashes`
3) IDE tab hack for html code:

    ```html
    div.container>div.row>div.col-md-4*3
    ```

   to

    ```html
    
    <div class="container">
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4"></div>
            <div class="col-md-4"></div>
        </div>
    </div>```

4) **Errors:** \
   a) sqlite3.ProgrammingError in IDE debug mode
    ```
    sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 9744 and this is thread id 12712.
    ```

   **Fix:** Play w/ `Allow parallel run` option for debug run config.

5) **IDE:**\

- debug flask, alembic and rest of the modules using python module with
  parameters;

6) **APP:**\

- In case flask app is executed in debug mode, then adding new model cls will
  automatically reflect the changes to DB without involving alembic migration
  revision.

7) **Utils:**\
   [appmap](https://plugins.jetbrains.com/plugin/16701-appmap) \
   AppMap is a free and open source visualization tool that allows you to see
   how your software works as it’s running.
   a) [Install AppMap for IDE](https://plugins.jetbrains.com/plugin/16701-appmap)
   \
   b) [Install the AppMap agent for Python](https://appland.com/docs/quickstart/pycharm/step-1)
   \

  ```sh
  npx @appland/appmap install-agent
  ? AppMap is about to be installed. Confirm the details below.
  Project type: poetry
  Project directory: projects/web_apps/pypi
  Git remote: origin    https://github.com/AleksNeStu/projects.git (fetch)
  Python version: 3.10.2
  Python package directory: projects/web_apps/pypi/.venv
  c) [Record AppMaps](https://appland.com/docs/quickstart/pycharm/step-3) \
    - [via tests](https://appland.com/docs/quickstart/pycharm/step-3-tests) \
    - [remote](https://appland.com/docs/quickstart/pycharm/step-3-remote) \
  ```   

## Tech-stack

<p align="center">
<img src="assets/diagram.png" alt="Stairway test">
</p>

> BE

- Python3


- [Jinja](https://github.com/pallets/jinja) \
  Jinja is a fast, expressive, extensible templating engine. Special
  placeholders in the template allow writing code similar to Python syntax.
  Then the template is passed data to render the final document. \
  [Jinja Templates](https://jinja.palletsprojects.com/en/3.0.x/templates/) \
  [jinja cheatsheet](https://devhints.io/jinja)


- [flask](https://github.com/pallets/flask) \
  Flask is a lightweight WSGI web application framework. It is designed to make
  getting started quick and easy, with the ability to scale up to complex
  applications. It began as a simple wrapper around Werkzeug and Jinja and has
  become one of the most popular Python web application frameworks. \
  Flask is better for quick development use cases and is perfect for
  prototyping. It is apt for developing microservices or serverless
  applications. \
  [Flask layout](https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/) \
  [Advanced patterns for views and routing](http://exploreflask.com/en/latest/views.html) \
  `FLASK_DEBUG=1` - auto-reload the flask app when a code change happens
  `FLASK_DEBUG=0` - to debug via IDE instead of seeing stacktrace in browser \
  [Flask 2 time run issue](https://stackoverflow.com/questions/25504149/why-does-running-the-flask-dev-server-run-itself-twice) \
  [flask-mail](https://github.com/mattupstate/flask-mail) \
  [flask-sijax](https://github.com/spantaleev/flask-sijax) \
  [flask-admin](https://github.com/flask-admin/flask-admin) \
  [Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) \
  [Flask-Social](https://github.com/mattupstate/flask-social/) \
  [WTForms](https://github.com/wtforms/flask-wtf/) \
  [Flask-MongoEngine](https://github.com/MongoEngine/flask-mongoengine) \
  **API:**
  https://flask-restful.readthedocs.io/en/latest/
  https://flask-restx.readthedocs.io/en/latest/
  https://github.com/zalando/connexion
  [Flask-DebugToolbar](https://flask-debugtoolbar.readthedocs.io/en/latest/) \

- [Werkzeug](https://github.com/pallets/werkzeug) \
  Werkzeug is a comprehensive WSGI web application library. It began as a
  simple collection of various utilities for WSGI applications and has become
  one of the most advanced WSGI utility libraries.


- [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) \
  SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
  application developers the full power and flexibility of SQL. SQLAlchemy
  provides a full suite of well known enterprise-level persistence patterns,
  designed for efficient and high-performing database access, adapted into a
  simple and Pythonic domain language. \
  [SQLAlchemy Docs](https://docs.sqlalchemy.org/en/14/) \
  [Key Features of SQLAlchemy](https://www.sqlalchemy.org/features.html) \
  [Engine, Connection, Session](https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference) \
  [sqlacodegen](https://github.com/agronholm/sqlacodegen) \
  This is a tool that reads the structure of an existing database and generates
  the appropriate SQLAlchemy model code, using the declarative style if
  possible. \
-
<p align="center">
<img src="assets/orm_core.png" alt="ORM and Core">
</p>

[Engine Configuration](https://docs.sqlalchemy.org/en/13/core/engines.html)
<p align="center">
<img src="assets/sqla_engine_arch.png" alt="Engine Configuration">
</p>

**ORM queries**
<p align="center">
<img src="assets/sql-1.png" alt="ORM queries" width="90%">
</p>

- Linux


- [Nginx / uWSGI]()

  <p>uWSGI is a software application that "aims at developing a full stack for building hosting services".[3] It is named after the Web Server Gateway Interface (WSGI), which was the first plugin supported by the project.[3]\
  <p>uwsgi (all lowercase) is the native binary protocol that uWSGI uses to communicate with other servers.[4] \
  <p> uWSGI is often used for serving Python web applications in conjunction with web servers such as Cherokee and Nginx, which offer direct support for uWSGI's native uwsgi protocol.[5] For example, data may flow like this: HTTP client ↔ Nginx ↔ uWSGI ↔ Python app.\
  <p> Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.\
  [Deploy Flask app in Nginx using uWSGI — with architectural explanation](https://medium.com/@yekabotep/deploy-flask-app-in-nginx-using-uwsgi-with-architectural-explanation-2e24a41c030a)
  [How To Serve Flask Applications with uWSGI and Nginx on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) \
  [Developing a Flask API in a Docker container with uWSGI and NGINX](https://gabimelo.medium.com/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e) \
  

  <p align="center">
        <img src="assets/uwsgi.jpeg" alt="uWSGI" width="90%">
  </p>

> FE

- [HTML/CSS]()

- [Cookies](https://developer.chrome.com/docs/devtools/storage/cookies/) \


- [Bootstrap](https://github.com/twbs/bootstrap) \
  Sleek, intuitive, and powerful front-end framework for faster and easier web
  development. \
  Quickly design and customize responsive mobile-first sites with Bootstrap,
  the world’s most popular front-end open source toolkit, featuring Sass
  variables and mixins, responsive grid system, extensive prebuilt components,
  and powerful JavaScript plugins. \
  [Get Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/download/) \
  [Buttons](https://getbootstrap.com/docs/4.0/components/buttons/) \

  **Alternatives:**
    - https://github.com/semantic-org/semantic-ui
    -


- [JS]
    - [jQuery](https://jquery.com/) \
      jQuery is a fast, small, and feature-rich JavaScript library. It makes
      things like HTML document traversal and manipulation, event handling,
      animation, and Ajax much simpler with an easy-to-use API that works
      across a multitude of browsers. With a combination of versatility and
      extensibility, jQuery has changed the way that millions of people write
      JavaScript. \

    - [popper](https://popper.js.org/) \
      Popper.js is a positioning engine, its purpose is to calculate the
      position of an element to make it possible to position it near a given
      reference element. \
      Popper.js has zero dependencies. No jQuery, no LoDash, nothing. It's used
      by big companies like Twitter in Bootstrap v4, Microsoft in WebClipper
      and Atlassian in AtlasKit. \
      Some of the key points are:
        - Position elements keeping them in their original DOM context (doesn't
          mess with your DOM!);
        - Allows to export the computed information to integrate with React and
          other view libraries;
        - Supports Shadow DOM elements;
        - Completely customizable thanks to the modifiers based structure;

    - [Vue.js](https://github.com/vuejs/vue) \
      Vue.js is a progressive, incrementally-adoptable JavaScript framework for
      building UI on the web.

> DB

- [PostgreSQL](https://github.com/postgres/postgres) \
  This directory contains the source code distribution of the PostgreSQL
  database management system. \
  PostgreSQL is an advanced object-relational database management system that
  supports an extended subset of the SQL standard, including transactions,
  foreign keys, subqueries, triggers, user-defined types and functions. This
  distribution also contains C language bindings.


- [Migrations]()
  [alembic](https://github.com/sqlalchemy/alembic) \


- [Query language]()

## Topics

1) Setup and tools
2) Introduction to Flask web framework
3) Creating our first site
4) HTML templates
5) Mapping URLs to methods
6) Bootstrap front-end framework
7) Data access with SQLAlchemy ORM
8) Database migrations with Alembic
9) User input with HTML forms
10) Server and client validation
11) Testing
    [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) \
    [WebTest](https://docs.pylonsproject.org/projects/webtest/en/latest/) \
    [pytest-clarity](https://github.com/darrenburns/pytest-clarity) \
    [Testing Flask Applications with Pytest](https://testdriven.io/blog/flask-pytest/) \
    [Flask-Testing](https://pythonhosted.org/Flask-Testing/) 
12) Deployment
13) MongoDB version
[Install](https://citizix.com/how-to-install-mongodb-5-on-fedora-34-35/) 
```sh
sudo rm -rf /tmp/mongodb-27017.sock
sudo service mongod start
 ```    
[RPM](https://repo.mongodb.org/yum/redhat/8Server/mongodb-org/5.0/x86_64/RPMS/) 
[ORM mongoengine](http://mongoengine.org/) 
MongoEngine is an Object-Document Mapper, written in Python for working with MongoDB. \
[BSON](https://en.wikipedia.org/wiki/BSON) \
[JSON and BSON](https://www.mongodb.com/json-and-bson) \
JavaScript objects are simple associative containers, wherein a string key is mapped to a value (which can be a number, string, function, or even another object). This simple language trait allowed JavaScript objects to be represented remarkably simply in text: \

JSON shows up in many different cases.
```
-APIs
-Configuration files
-Log messages
-Database storage 
```

However, there are several issues that make JSON less than ideal for usage 
inside of a database.
```
-JSON is a text-based format, and text parsing is very slow
-JSON’s readable format is far from space-efficient, another database concern
-JSON only supports a limited number of basic data types
```

**BSON** simply stands for “Binary JSON,” and that’s exactly what it was invented to be. BSON’s binary structure encodes type and length information, which allows it to be parsed much more quickly.
```
-Firstly, JSON documents are polymorphic – fields can vary from document to document within a single collection (analogous to table in a relational database). Documents make modeling diverse record attributes easy for developers, elegantly handling data of any structure.
-Secondly, there is no need to declare the structure of documents to the database – documents are self-describing. Developers can start writing code and persist objects as they are created.
-Thirdly, if a new field needs to be added to a document, it can be created without affecting all other documents in the collection, without updating a central system catalog and without taking the database offline. When you need to make changes to the data model, the document database continues to store the updated objects without the need to perform costly ALTER TABLE operations – or worse, having to redesign the schema from scratch.
```


**Alternatives:**
MongoKit vs MongoEngine vs Flask-MongoAlchemy for Flask
[Flask-MongoAlchemy](https://github.com/cobrateam/flask-mongoalchemy) 
```sh
# get db dir
grep -i dbPath /etc/mongod.conf
# dbPath: /var/lib/mongo
```
[Robo 3T is the MongoDB GUI for hobbyists](https://robomongo.org/) 
```
patchelf --replace-needed libcurl-gnutls.so.4 libcurl.so.4 robo3t
ln -s /usr/lib64/libcurl.so.4 ~/robo3t-1.4.1.../lib/libcurl-gnutls.so.4
sudo ln -s /opt/robo3t/bin/robo3t /usr/local/bin/robo3t
```
[Studio 3T is the MongoDB IDE for professionals](https://studio3t.com/download-studio-3t/) 

## Requirements

1) **Python 3.x**
2) **poetry** - Dependency Management for Python.

# Description

<p align="center">
<img src="assets/model-view-controller.png" alt="MVC (Model-View-Controller)">
</p>

**MVC (Model-View-Controller)** is a pattern in software design commonly used
to implement user interfaces, data, and controlling logic. It emphasizes a
separation between the software’s business logic and display. This "separation
of concerns" provides for a better division of labor and improved maintenance.\

**Building Blocks of Flask**

1) **Routes:** Map URL patterns to views app.route maps URLs to views with a
   unique url pattern, optional HTTP verb, and route data.


2) **Controllers (View methods):** Process request


3) **Views (Templates):** Dynamic HTML Data passed to templates are keyword
   arguments. Can include data and methods.


4) **Models:** Data and behavior passed to view


5) **Static content:** Rich support for cached assets

   Static files will automatically be served from /static/...


6) **Configuration:** Dev, test, prod configs
