Skip to main contentAccessibility help
Accessibility feedback
￼￼
**[A]**
- [ACID](https://en.wikipedia.org/wiki/ACID) \
  ACID (atomicity, consistency, isolation, durability) is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps.
- [CAP](https://www.geeksforgeeks.org/the-cap-theorem-in-dbms/) \
  The three letters in CAP refer to three desirable properties of distributed systems with replicated data: consistency (among replicated copies), availability of the system for read and write operations) and partition tolerance in the face of the nodes in the system being partitioned by a network fault).

**[B]**
- [b-tree index](https://dzone.com/articles/database-btree-indexing-in-sqlite) \
  In computer science, a B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.

**[C]**
> Compare
 - [https://stackoverflow.com/questions/19251910/difference-between-sql-and-dump-files](https://stackoverflow.com/questions/3840908/how-do-i-see-the-differences-between-2-mysql-dumps) \

**[D]**
> Databases
---
- [MongoDB](https://www.mongodb.com/) \
    MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License
  > async
  - [μMongo](https://github.com/Scille/umongo) \
    μMongo: sync/async ODM
    Mongo is a Python MongoDB ODM. It inception comes from two needs: the lack of async ODM and the difficulty to do document (un)serialization with existing ODMs.
    From this point, μMongo made a few design choices:
    Stay close to the standards MongoDB driver to keep the same API when possible: use find({"field": "value"}) like usual but retrieve your data nicely OO wrapped !
    Work with multiple drivers (PyMongo, TxMongo, motor_asyncio and mongomock for the moment)
    Tight integration with Marshmallow serialization library to easily dump and load your data with the outside world
    i18n integration to localize validation error messages
    Free software: MIT license
    Test with 90%+ coverage ;-)
    µMongo requires MongoDB 4.2+ and Python 3.7+.

---
- [PostgreSQL](https://www.postgresql.org/) \
    PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley.
  > sync
  - [psycopg2](https://pypi.org/project/psycopg2/) \
    Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.
    Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being both efficient and secure. It features client-side and server-side cursors, asynchronous communication and notifications, “COPY TO/COPY FROM” support. Many Python types are supported out-of-the-box and adapted to matching PostgreSQL data types; adaptation can be extended and customized thanks to a flexible objects adaptation system.
      Psycopg 2 is both Unicode and Python 3 friendly.

  > async
  - [aiopg](https://pypi.org/project/aiopg/) \
    aiopg is a library for accessing a PostgreSQL database from the asyncio (PEP-3156/tulip) framework. It wraps asynchronous features of the Psycopg database driver.
  - [asyncpg](https://github.com/MagicStack/asyncpg) \
    asyncpg -- A fast PostgreSQL Database Client Library for Python/asyncio
    asyncpg is a database interface library designed specifically for PostgreSQL and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL server binary protocol for use with Python's asyncio framework. You can read more about asyncpg in an introductory blog post.
    asyncpg requires Python 3.6 or later and is supported for PostgreSQL versions 9.5 to 13. Older PostgreSQL versions or other databases implementing the PostgreSQL protocol may work, but are not being actively tested.
  - [psycopg3](https://www.psycopg.org/psycopg3/docs/advanced/async.html) \
    Psycopg Connection and Cursor have counterparts AsyncConnection and AsyncCursor supporting an asyncio interface.
      The design of the asynchronous objects is pretty much the same of the sync ones: in order to use them you will only have to scatter the await keyword here and there.
      Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python.
    

---
- [Database File System](https://docs.oracle.com/database/121/ADLOB/adlob_fs.htm#ADLOB45943) \
  Database File System (DBFS) creates a standard file system interface on top of files and directories that are stored in database tables.
  Database File System (DBFS) creates a standard file system interface using a server and clients.

---
- [Redis](https://redis.io/) \
  Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.
  > async
  - [asyncio-redis](https://github.com/jonathanslenders/asyncio-redis) \
    Redis client for Python asyncio.
    Redis client for the PEP 3156 Python event loop.
    This Redis library is a completely asynchronous, non-blocking client for a Redis server. It depends on asyncio (PEP 3156) and requires Python 3.6 or greater. If you're new to asyncio, it can be helpful to check out the asyncio documentation first.
---


**[E]**


**[F]**
> Frameworks
---
**Microframeworks**
- [bottle](https://github.com/bottlepy/bottle) \
  Bottle is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.

  Routing: Requests to function-call mapping with support for clean and dynamic URLs.
Templates: Fast and pythonic *built-in template engine* and support for mako, jinja2 and cheetah templates.

  Utilities: Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.
  Server: Built-in HTTP development server and support for paste, fapws3, bjoern, Google App Engine, cherrypy or any other WSGI capable HTTP server.

- [flask](https://github.com/pallets/flask)

  Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

- [pyramid](https://github.com/Pylons/pyramid)

  Pyramid is a small, fast, down-to-earth, open source Python web framework. It makes real-world web application development and deployment more fun, more predictable, and more productive.
---
**Building block frameworks**
- [django](https://github.com/django/django)

  Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

**[G]**


**[H]**

**[I]**
> Index
- [Database index](https://en.wikipedia.org/wiki/Database_index)
- [+-](https://vanseodesign.com/web-design/mysql-indexes/)

**[J]**

**[K]**

**[L]**

**[M]**
> Migrations
- [yoyo-migrations](https://pypi.org/project/yoyo-migrations/) \
  Yoyo-migrations is a database schema migration tool. Database migrations can be written as SQL files or Python scripts.
- [alembic](https://alembic.sqlalchemy.org/en/latest/autogenerate.html) \
  Alembic can view the status of the database and compare against the table metadata in the application, generating the “obvious” migrations based on a comparison. This is achieved using the --autogenerate option to the alembic revision command, which places so-called candidate migrations into our new migrations file. We review and modify these by hand as needed, then proceed normally.
- [zero downtime](https://spring.io/blog/2016/05/31/zero-downtime-deployment-with-a-database) \
    Zero Downtime Deployment
- [backward compatibility migrations](https://thorben-janssen.com/update-database-schema-without-downtime/#Backward-Compatible_Operations) \


**[N]**
> Normalization
- [DB Normalization](https://www.guru99.com/database-normalization.html) \
  Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like Insertion, Update and Deletion Anomalies. Normalization rules divides larger tables into smaller tables and links them using relationships. The purpose of Normalisation in SQL is to eliminate redundant (repetitive) data and ensure data is stored logically.

> NoSQL
- [Introduction to NoSQL](https://www.geeksforgeeks.org/introduction-to-nosql/)
- [Use of NoSQL in Industry](https://www.geeksforgeeks.org/use-of-nosql-in-industry/)
- [NoSQL Data Architecture Patterns](https://www.geeksforgeeks.org/nosql-data-architecture-patterns/)
- [NoSQL](https://en.wikipedia.org/wiki/NoSQL)
  > Key–value store
  - Memcached, Redis, Coherence, DynamoDB, Berkeley DB
  > Document store (Column Store Database)
  - [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
  - CouchDB, Cloudant, HBase, Bigtable by Google
  > Graph
  - Neo4J, FlockDB( Used by Twitter)
  > Column Store Database (Tabular)
  - Hbase, Accumulo, HBase, Bigtable by Google, Cassandra

> NewSQL
- [NewSQL DB](https://en.wikipedia.org/wiki/NewSQL)
- [Difference between NoSQL and NewSQL](https://www.geeksforgeeks.org/difference-between-nosql-and-newsql/)

> SQL vs NoSQL
- [SQL vs NoSQL: Which one is better to use?](https://www.geeksforgeeks.org/sql-vs-nosql-which-one-is-better-to-use/)
- [Difference between SQL and NoSQL](https://www.geeksforgeeks.org/difference-between-sql-and-nosql/)

**[O]**
> ORM
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/) \
  The Python SQL Toolkit and Object Relational Mapper
  SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. SQLAlchemy provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.
- [SQLAlchemy articles](https://shravan-kuchkula.github.io/tags/#sqlalchemy)


**[P]**
> Problems
- [Concurrency problems in DBMS Transactions](https://www.geeksforgeeks.org/concurrency-problems-in-dbms-transactions/)
- [Transaction Isolation Levels in DBMS](https://www.geeksforgeeks.org/transaction-isolation-levels-dbms/)

**[Q]**
> Query builder
- [pypika](https://github.com/kayak/pypika) \
  PyPika is a Python API for building SQL queries. The motivation behind PyPika is to provide a simple interface for building SQL queries without limiting the flexibility of handwritten SQL.

> Query
- [GraphQuery](https://github.com/storyicon/graphquery) \
  GraphQuery is a query language and execution engine tied to any backend service. It is back-end language independent.




**[R]**
> Replication
- [Data Replication in DBMS](https://www.geeksforgeeks.org/data-replication-in-dbms/)


**[S]**
> Sharding
- [Database Sharding – System Design Interview Concept](https://www.geeksforgeeks.org/database-sharding-a-system-design-concept/)
- [Apache ZooKeeper](https://en.wikipedia.org/wiki/Apache_ZooKeeper)

> Scaling
- [Horizontal and Vertical Scaling In Databases](https://www.geeksforgeeks.org/horizontal-and-vertical-scaling-in-databases/)

> Study
- [Difference between OLAP and OLTP in DBMS](https://www.geeksforgeeks.org/difference-between-olap-and-oltp-in-dbms/)

> SQL commands
- [EXPLAIN](https://www.exoscale.com/syslog/explaining-mysql-queries/)
- [EXPLAIN ANALYZE](https://mysqlserverteam.com/mysql-explain-analyze/)

> SQL commands [types]
- [SQL | DDL, DQL, DML, DCL and TCL Commands](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
- [Difference between DDL and DML in DBMS](https://www.geeksforgeeks.org/difference-between-ddl-and-dml-in-dbms/)

**[T]**
> 2PC
- [Two-phase commit protocol](https://en.wikipedia.org/wiki/Two-phase_commit_protocol)
- [Two Phase Commit Protocol (Distributed Transaction Management](https://www.geeksforgeeks.org/two-phase-commit-protocol-distributed-transaction-management/)
- [Three Phase Commit Protocol](https://www.geeksforgeeks.org/three-phase-commit-protocol/)
- [https://www.geeksforgeeks.org/recovery-from-failures-in-two-phase-commit-protocol-distributed-transaction/](https://www.geeksforgeeks.org/recovery-from-failures-in-two-phase-commit-protocol-distributed-transaction/)

> 3PC
- [Three-phase commit protocol](https://en.wikipedia.org/wiki/Three-phase_commit_protocol)
- [DTP!](https://habr.com/ru/post/431854/)
- [s](https://habr.com/ru/company/otus/blog/506072/)

**[U]**

**[V]**
> VCS
- [flywaydb]

**[W]**
> WSGI (Web Server Gateway Interface) (https://wsgi.readthedocs.io/en/latest/)

The Web Server Gateway Interface (WSGI, pronounced whiskey[1][2] or WIZ-ghee[3]) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. The current version of WSGI, version 1.0.1, is specified in Python Enhancement Proposal (PEP) 3333.[4]
WSGI was originally specified as PEP-333 in 2003.[5] PEP-3333, published in 2010, updates the specification for Python 3.
---
- [flask](https://github.com/pallets/flask) \
  Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.\
  - [jinja](https://jinja.palletsprojects.com/en/3.0.x/) \
  Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document. \
  - [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) \
  werkzeug German noun: “tool”. Etymology: werk (“work”), zeug (“stuff”)
Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.
Werkzeug doesn’t enforce any dependencies. It is up to the developer to choose a template engine, database adapter, and even how to handle requests. \
  - [async flask](https://flask.palletsprojects.com/en/2.0.x/async-await/) \
  Routes, error handlers, before request, after request, and teardown functions can all be coroutine functions if Flask is installed with the async extra (pip install flask[async]). It requires Python 3.7+ where contextvars.ContextVar is available. This allows views to be defined with async def and use await.
  ```
  @app.route("/get-data")
  async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
  ```
  Performance
  Async functions require an event loop to run. Flask, as a WSGI application, uses one worker to handle one request/response cycle. When a request comes in to an async view, Flask will start an event loop in a thread, run the view function there, then return the result.\
  Each request still ties up one worker, even for async views. The upside is that you can run async code within a view, for example to make multiple concurrent database queries, HTTP requests to an external API, etc. However, the number of requests your application can handle at one time will remain the same.\
  Async is not inherently faster than sync code. Async is beneficial when performing concurrent IO-bound tasks, but will probably not improve CPU-bound tasks. Traditional Flask views will still be appropriate for most use cases, but Flask’s async support enables writing and using code that wasn’t possible natively before.
  Background tasks
  Async functions will run in an event loop until they complete, at which stage the event loop will stop. This means any additional spawned tasks that haven’t completed when the async function completes will be cancelled. Therefore you cannot spawn background tasks, for example via asyncio.create_task.\
  If you wish to use background tasks it is best to use a task queue to trigger background work, rather than spawn tasks in a view function. With that in mind you can spawn asyncio tasks by serving Flask with an ASGI server and utilising the asgiref WsgiToAsgi adapter as described in ASGI. This works as the adapter creates an event loop that runs continually.
  When to use Quart instead\
  Flask’s async support is less performant than async-first frameworks due to the way it is implemented. If you have a mainly async codebase it would make sense to consider Quart. Quart is a reimplementation of Flask based on the ASGI standard instead of WSGI. This allows it to handle many concurrent requests, long running requests, and websockets without requiring multiple worker processes or threads.\
  https://flask.palletsprojects.com/en/2.0.x/deploying/asgi/#asgi
  If you’d like to use an ASGI server you will need to utilise WSGI to ASGI middleware. The asgiref WsgiToAsgi adapter is recommended as it integrates with the event loop used for Flask’s Using async and await support. You can use the adapter by wrapping the Flask app\
  It has also already been possible to run Flask with Gevent or Eventlet to get many of the benefits of async request handling. These libraries patch low-level Python functions to accomplish this, whereas async/ await and ASGI use standard, modern Python capabilities. Deciding whether you should use Flask, Quart, or something else is ultimately up to understanding the specific needs of your project. \

  - [quart](https://gitlab.com/pgjones/quart) \
  Quart is a Python ASGI web microframework with the same API as Flask.\
  Quart is an async Python web microframework. Using Quart you can,
  render and serve HTML templates,
  write (RESTful) JSON APIs,
  serve WebSockets,
  stream request and response data,
  do pretty much anything over the HTTP or WebSocket protocols. \
  Flask’s async support is less performant than async-first frameworks due to the way it is implemented. If you have a mainly async codebase it would make sense to consider Quart. Quart is a reimplementation of Flask based on the ASGI standard instead of WSGI. This allows it to handle many concurrent requests, long running requests, and websockets without requiring multiple worker processes or threads. \
It has also already been possible to run Flask with Gevent or Eventlet to get many of the benefits of async request handling. These libraries patch low-level Python functions to accomplish this, whereas async/ await and ASGI use standard, modern Python capabilities. Deciding whether you should use Flask, Quart, or something else is ultimately up to understanding the specific needs of your project.
---
- [gunicorn](https://gunicorn.org/) \
  Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
---
> ASGI (Asynchronous Server Gateway Interface) 

ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.\
Where WSGI provided a standard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous apps, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.\
You can read more in the introduction to ASGI, look through the specifications, and see what implementations there already are or that are upcoming.


- [asgiref](https://github.com/django/asgiref) \
  ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI. You can read more at https://asgi.readthedocs.io/en/latest/
This package includes ASGI base libraries, such as:
Sync-to-async and async-to-sync function wrappers, asgiref.sync
Server base classes, asgiref.server
A WSGI-to-ASGI adapter, in asgiref.wsgi


- [hypercorn](https://gitlab.com/pgjones/hypercorn) \
  Hypercorn is an ASGI Server based on Hyper libraries and inspired by Gunicorn.
  Hypercorn is an ASGI web
  server based on the sans-io hyper, h11, h2, and wsproto libraries and inspired by
  Gunicorn. Hypercorn supports HTTP/1, HTTP/2, WebSockets (over HTTP/1
  and HTTP/2), ASGI/2, and ASGI/3 specifications. Hypercorn can utilise
  asyncio, uvloop, or trio worker types.
  Hypercorn can optionally serve the current draft of the HTTP/3
  specification using the aioquic library. To enable this install
  the h3 optional extra, pip install hypercorn[h3] and then
  choose a quic binding e.g. hypercorn --quic-bind localhost:4433
  ....
  Hypercorn was initially part of Quart before being separated out into a
  standalone ASGI server. Hypercorn forked from version 0.5.0 of Quart.
 

- [Uvicorn](https://www.uvicorn.org/) \
  Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. \
Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks. \
ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI. \
Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned. \


- [Daphne](https://github.com/django/daphne) \
  Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP, developed to power Django Channels. \
It supports automatic negotiation of protocols; there's no need for URL prefixing to determine WebSocket endpoints versus HTTP endpoints.




**[X]**

**[Y]**

**[Z]**