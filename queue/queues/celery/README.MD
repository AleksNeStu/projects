# I) URLS
### Desc
https://www.toptal.com/python/orchestrating-celery-python-background-jobs

### Libs
http://eventlet.net/
http://www.gevent.org/
https://github.com/celery/celery

https://github.com/sontek/pyramid_celery
https://pypi.org/project/celery-pylons/
https://code.google.com/archive/p/web2py-celery/
https://github.com/mher/tornado-celery/


### Docs
https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html
https://docs.celeryq.dev/en/latest/


# II) Description
Celery is a task queue that allows you to schedule and execute long-running tasks asynchronously using worker processes. It is often used in web applications to offload long-running tasks to a separate process, so that the main web server can continue to respond to requests quickly.

Celery and RabbitMQ are some tools used in in event-driven architectures.\
Celery’s asynchronous task queue allows the execution of tasks and its concurrency makes it useful in several production systems.

Celery is one of the most popular background job managers in the Python world. Celery is compatible with several message brokers like RabbitMQ or Redis and can act as both producer and consumer.

Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operations but supports scheduling as well. The execution units, called tasks, are executed concurrently on one or more worker servers **using multiprocessing, Eventlet, or gevent.** Tasks can execute asynchronously (in the background) or synchronously (wait until ready)

Celery, like a consumer appliance, doesn’t need much configuration to operate. It has an input and an output. The input must be connected to a broker, and the output can be optionally connected to a result backend. However, if you look closely at the back, there’s a lid revealing loads of sliders, dials, and buttons: this is the configuration.


A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

Celery is written in Python, but the protocol can be implemented in any language. In addition to Python there's [node-celery](https://github.com/mher/node-celery) for Node.js, a [PHP client](https://github.com/gjedeer/celery-php), [gocelery](https://github.com/gocelery/gocelery) for golang, and [rusty-celery](https://github.com/rusty-celery/rusty-celery) for Rust.

Language interoperability can also be achieved by using webhooks in such a way that the client enqueues an URL to be requested by a worker.


_Celery_ is usually used with a message broker to send and receive messages. The RabbitMQ, Redis transports are feature complete, but there's also experimental support for a myriad of other solutions, including using SQLite for local development.

Celery can run on a single machine, on multiple machines, or even across datacenters.

## Supports

> -   **Message Transports**
      >
      >     > -   [RabbitMQ](https://rabbitmq.com), [Redis](https://redis.io), Amazon SQS
>
> -   **Concurrency**
      >
      >     > -   Prefork, [Eventlet](http://eventlet.net/), [gevent](http://gevent.org/), single threaded (`solo`)
>
> -   **Result Stores**
      >
      >     > -   AMQP, Redis
      >     > -   memcached
      >     > -   SQLAlchemy, Django ORM
      >     > -   Apache Cassandra, IronCache, Elasticsearch
>
> -   **Serialization**
      >
      >     > -   _pickle_, _json_, _yaml_, _msgpack_.
      >     > -   _zlib_, _bzip2_ compression.
      >     > -   Cryptographic message signing.
>

## Framework Integration

Celery is easy to integrate with web frameworks, some of which even have integration packages:

> <table><tbody valign="top"><tr><td><a href="https://djangoproject.com/" rel="nofollow">Django</a></td><td>not needed</td></tr><tr><td><a href="http://docs.pylonsproject.org/en/latest/docs/pyramid.html" rel="nofollow">Pyramid</a></td><td><a href="https://pypi.org/project/pyramid_celery/" rel="nofollow">pyramid_celery</a></td></tr><tr><td><a href="http://pylonsproject.org/" rel="nofollow">Pylons</a></td><td><a href="https://pypi.org/project/celery-pylons/" rel="nofollow">celery-pylons</a></td></tr><tr><td><a href="http://flask.pocoo.org/" rel="nofollow">Flask</a></td><td>not needed</td></tr><tr><td><a href="http://web2py.com/" rel="nofollow">web2py</a></td><td><a href="https://code.google.com/p/web2py-celery/" rel="nofollow">web2py-celery</a></td></tr><tr><td><a href="http://www.tornadoweb.org/" rel="nofollow">Tornado</a></td><td><a href="https://github.com/mher/tornado-celery/">tornado-celery</a></td></tr></tbody></table>

### Bundles

Celery also defines a group of bundles that can be used to install Celery and the dependencies for a given feature.


# III) Usage
1) Instagram uses Celery to scale thousands of tasks to millions
2) Bbackground mailing
3) Report generation
4) Logging
5) Error reporting.




# IV) Pros
1) open-source task queue software written in Python
2) incredibly lightweight
3) supports multiple brokers (RabbitMQ, Redis, Amazon SQS, etc)
4) integrates with many web frameworks (Django, etc)

# V) Cons
1) Simple: Celery is easy to use and maintain, and does not need configuration files.
2) Highly Available: workers and clients will automatically retry in the event of connection loss or failure, and some brokers support HA in way of Primary/Primary or Primary/Replica replication.
3) Fast: A single Celery process can process millions of tasks a minute, with sub-millisecond round-trip latency (using RabbitMQ, py-librabbitmq, and optimized settings).
4) Flexible: Almost every part of Celery can be extended or used on its own, Custom pool implementations, serializers, compression schemes, logging, schedulers, consumers, producers, broker transports, and much more.
5) Supports: Message Transports, Concurrency, Result Stores, Serialization
6) Framework Integration: Django - not needed, Pyramid - pyramid_celery, Pylons	- celery-pylons, Flask - not needed, web2py	web2py-celery, Tornado	tornado-celery
7) Bundles: Celery also defines a group of bundles that can be used to install Celery and the dependencies for a given feature.


# VI) Compare
1) Diff1
2) Diff2

# VII) Tips
- Set up a separate worker process to handle tasks. This will allow you to scale your application horizontally by adding more worker processes as needed.
- Use a message broker, such as RabbitMQ or Redis, to manage communication between the web server and the worker processes.
- Use the "retry" feature to automatically retry tasks that fail due to transient errors, such as network issues or temporary resource unavailability.
- Use the "rate_limit" feature to limit the number of tasks that can be processed concurrently, to avoid overloading your system.
- Use the "timeouts" feature to specify a maximum execution time for tasks, to prevent them from running indefinitely.
