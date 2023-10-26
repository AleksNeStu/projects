![image](https://docs.celeryq.dev/en/latest/_images/celery-banner-small.png)

[![Build status](https://github.com/celery/celery/actions/workflows/python-package.yml/badge.svg)](https://github.com/celery/celery/actions/workflows/python-package.yml)
[![coverage](https://codecov.io/github/celery/celery/coverage.svg?branch=master)](https://codecov.io/github/celery/celery?branch=master)
[![BSD License](https://img.shields.io/pypi/l/celery.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Celery can be installed via wheel](https://img.shields.io/pypi/wheel/celery.svg)](https://pypi.org/project/celery/)
[![Supported Python versions.](https://img.shields.io/pypi/pyversions/celery.svg)](https://pypi.org/project/celery/)
[![Supported Python implementations.](https://img.shields.io/pypi/implementation/celery.svg)](https://pypi.org/project/celery/)
[![Backers on Open Collective](https://opencollective.com/celery/backers/badge.svg)](#backers)
[![Sponsors on Open Collective](https://opencollective.com/celery/sponsors/badge.svg)](#sponsors)

Version

:   5.3.0b1 (dawn-chorus)

Web

:   <https://docs.celeryq.dev/en/stable/index.html>

Download

:   <https://pypi.org/project/celery/>

Source

:   <https://github.com/celery/celery/>

Keywords

:   task, queue, job, async, rabbitmq, amqp, redis, python, distributed,
    actors

# Donations

This project relies on your generous donations.

If you are using Celery to create a commercial product, please consider
becoming our [backer](https://opencollective.com/celery#backer) or our
[sponsor](https://opencollective.com/celery#sponsor) to ensure Celery\'s
future.

# For enterprise

Available as part of the Tidelift Subscription.

The maintainers of `celery` and thousands of other packages are working
with Tidelift to deliver commercial support and maintenance for the open
source dependencies you use to build your applications. Save time,
reduce risk, and improve code health, while paying the maintainers of
the exact dependencies you use. [Learn
more.](https://tidelift.com/subscription/pkg/pypi-celery?utm_source=pypi-celery&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)

# What\'s a Task Queue?

Task queues are used as a mechanism to distribute work across threads or
machines.

A task queue\'s input is a unit of work, called a task, dedicated worker
processes then constantly monitor the queue for new work to perform.

Celery communicates via messages, usually using a broker to mediate
between clients and workers. To initiate a task a client puts a message
on the queue, the broker then delivers the message to a worker.

A Celery system can consist of multiple workers and brokers, giving way
to high availability and horizontal scaling.

Celery is written in Python, but the protocol can be implemented in any
language. In addition to Python there\'s
[node-celery](https://github.com/mher/node-celery) for Node.js, a [PHP
client](https://github.com/gjedeer/celery-php),
[gocelery](https://github.com/gocelery/gocelery) for golang, and
[rusty-celery](https://github.com/rusty-celery/rusty-celery) for Rust.

Language interoperability can also be achieved by using webhooks in such
a way that the client enqueues an URL to be requested by a worker.

# What do I need?

Celery version 5.3.0a1 runs on,

-   Python (3.7, 3.8, 3.9, 3.10)
-   PyPy3.7 (7.3.7+)

This is the version of celery which will support Python 3.7 or newer.

If you\'re running an older version of Python, you need to be running an
older version of Celery:

-   Python 3.6: Celery 5.1 or earlier.
-   Python 2.7: Celery 4.x series.
-   Python 2.6: Celery series 3.1 or earlier.
-   Python 2.5: Celery series 3.0 or earlier.
-   Python 2.4: Celery series 2.2 or earlier.

Celery is a project with minimal funding, so we don\'t support Microsoft
Windows. Please don\'t open any issues related to that platform.

*Celery* is usually used with a message broker to send and receive
messages. The RabbitMQ, Redis transports are feature complete, but
there\'s also experimental support for a myriad of other solutions,
including using SQLite for local development.

*Celery* can run on a single machine, on multiple machines, or even
across datacenters.

# Get Started

If this is the first time you\'re trying to use Celery, or you\'re new
to Celery v5.3.0a1 coming from previous versions then you should read
our getting started tutorials:

-   [First steps with
    Celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

    > Tutorial teaching you the bare minimum needed to get started with
    > Celery.

-   [Next
    steps](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html)

    > A more complete overview, showing more features.

> You can also get started with Celery by using a hosted broker
> transport CloudAMQP. The largest hosting provider of RabbitMQ is a
> proud sponsor of Celery.

# Celery is\...

-   **Simple**

    > Celery is easy to use and maintain, and does *not need
    > configuration files*.
    >
    > It has an active, friendly community you can talk to for support,
    > like at our [mailing-list](#mailing-list), or the IRC channel.
    >
    > Here\'s one of the simplest applications you can make:
    >
    > ``` python
    > from celery import Celery
    >
    > app = Celery('hello', broker='amqp://guest@localhost//')
    >
    > @app.task
    > def hello():
    >     return 'hello world'
    > ```

-   **Highly Available**

    > Workers and clients will automatically retry in the event of
    > connection loss or failure, and some brokers support HA in way of
    > *Primary/Primary* or *Primary/Replica* replication.

-   **Fast**

    > A single Celery process can process millions of tasks a minute,
    > with sub-millisecond round-trip latency (using RabbitMQ,
    > py-librabbitmq, and optimized settings).

-   **Flexible**

    > Almost every part of *Celery* can be extended or used on its own,
    > Custom pool implementations, serializers, compression schemes,
    > logging, schedulers, consumers, producers, broker transports, and
    > much more.

# It supports\...

> -   **Message Transports**
>
>     > -   [RabbitMQ](https://rabbitmq.com), [Redis](https://redis.io),
>     >     Amazon SQS
>
> -   **Concurrency**
>
>     > -   Prefork, [Eventlet](http://eventlet.net/),
>     >     [gevent](http://gevent.org/), single threaded (`solo`)
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
>     > -   *pickle*, *json*, *yaml*, *msgpack*.
>     > -   *zlib*, *bzip2* compression.
>     > -   Cryptographic message signing.

# Framework Integration

Celery is easy to integrate with web frameworks, some of which even have
integration packages:

>   ---------------------------------------------------------------------- ------------------------------------------------------------
>   [Django](https://djangoproject.com/)                                   not needed
>
>   [Pyramid](http://docs.pylonsproject.org/en/latest/docs/pyramid.html)   [pyramid_celery](https://pypi.org/project/pyramid_celery/)
>
>   [Pylons](http://pylonsproject.org/)                                    [celery-pylons](https://pypi.org/project/celery-pylons/)
>
>   [Flask](http://flask.pocoo.org/)                                       not needed
>
>   [web2py](http://web2py.com/)                                           [web2py-celery](https://code.google.com/p/web2py-celery/)
>
>   [Tornado](http://www.tornadoweb.org/)                                  [tornado-celery](https://github.com/mher/tornado-celery/)
>   ---------------------------------------------------------------------- ------------------------------------------------------------

The integration packages aren\'t strictly necessary, but they can make
development easier, and sometimes they add important hooks like closing
database connections at `fork`.

# Documentation {#celery-documentation}

The [latest documentation](https://docs.celeryq.dev/en/latest/) is
hosted at Read The Docs, containing user guides, tutorials, and an API
reference.

最新的中文文档托管在 <https://www.celerycn.io/>
中，包含用户指南、教程、API接口等。

# Installation {#celery-installation}

You can install Celery either via the Python Package Index (PyPI) or
from source.

To install using `pip`:

:

    $ pip install -U Celery

## Bundles

Celery also defines a group of bundles that can be used to install
Celery and the dependencies for a given feature.

You can specify these in your requirements or on the `pip` command-line
by using brackets. Multiple bundles can be specified by separating them
by commas.

:

    $ pip install "celery[amqp]"

    $ pip install "celery[amqp,redis,auth,msgpack]"

The following bundles are available:

### Serializers

`celery[auth]`

:   for using the `auth` security serializer.

`celery[msgpack]`

:   for using the msgpack serializer.

`celery[yaml]`

:   for using the yaml serializer.

### Concurrency

`celery[eventlet]`

:   for using the `eventlet` pool.

`celery[gevent]`

:   for using the `gevent` pool.

### Transports and Backends

`celery[amqp]`

:   for using the RabbitMQ amqp python library.

`celery[redis]`

:   for using Redis as a message transport or as a result backend.

`celery[sqs]`

:   for using Amazon SQS as a message transport.

`celery[tblib`\]

:   for using the `task_remote_tracebacks` feature.

`celery[memcache]`

:   for using Memcached as a result backend (using `pylibmc`)

`celery[pymemcache]`

:   for using Memcached as a result backend (pure-Python
    implementation).

`celery[cassandra]`

:   for using Apache Cassandra/Astra DB as a result backend with the
    DataStax driver.

`celery[azureblockblob]`

:   for using Azure Storage as a result backend (using `azure-storage`)

`celery[s3]`

:   for using S3 Storage as a result backend.

`celery[couchbase]`

:   for using Couchbase as a result backend.

`celery[arangodb]`

:   for using ArangoDB as a result backend.

`celery[elasticsearch]`

:   for using Elasticsearch as a result backend.

`celery[riak]`

:   for using Riak as a result backend.

`celery[cosmosdbsql]`

:   for using Azure Cosmos DB as a result backend (using `pydocumentdb`)

`celery[zookeeper]`

:   for using Zookeeper as a message transport.

`celery[sqlalchemy]`

:   for using SQLAlchemy as a result backend (*supported*).

`celery[pyro]`

:   for using the Pyro4 message transport (*experimental*).

`celery[slmq]`

:   for using the SoftLayer Message Queue transport (*experimental*).

`celery[consul]`

:   for using the Consul.io Key/Value store as a message transport or
    result backend (*experimental*).

`celery[django]`

:   specifies the lowest version possible for Django support.

    You should probably not use this in your requirements, it\'s here
    for informational purposes only.

## Downloading and installing from source {#celery-installing-from-source}

Download the latest version of Celery from PyPI:

<https://pypi.org/project/celery/>

You can install it by doing the following,:

:

    $ tar xvfz celery-0.0.0.tar.gz
    $ cd celery-0.0.0
    $ python setup.py build
    # python setup.py install

The last command must be executed as a privileged user if you aren\'t
currently using a virtualenv.

## Using the development version {#celery-installing-from-git}

### With pip

The Celery development version also requires the development versions of
`kombu`, `amqp`, `billiard`, and `vine`.

You can install the latest snapshot of these using the following pip
commands:

:

    $ pip install https://github.com/celery/celery/zipball/master#egg=celery
    $ pip install https://github.com/celery/billiard/zipball/master#egg=billiard
    $ pip install https://github.com/celery/py-amqp/zipball/master#egg=amqp
    $ pip install https://github.com/celery/kombu/zipball/master#egg=kombu
    $ pip install https://github.com/celery/vine/zipball/master#egg=vine

### With git

Please see the Contributing section.

# Getting Help

## Mailing list

For discussions about the usage, development, and future of Celery,
please join the
[celery-users](https://groups.google.com/group/celery-users/) mailing
list.

## IRC {#irc-channel}

Come chat with us on IRC. The **#celery** channel is located at the
[Libera Chat](https://libera.chat/) network.

# Bug tracker

If you have any suggestions, bug reports, or annoyances please report
them to our issue tracker at <https://github.com/celery/celery/issues/>

# Wiki

<https://github.com/celery/celery/wiki>

# Credits

## Contributors {#contributing-short}

This project exists thanks to all the people who contribute. Development
of [celery]{.title-ref} happens at GitHub:
<https://github.com/celery/celery>

You\'re highly encouraged to participate in the development of
[celery]{.title-ref}. If you don\'t like GitHub (for some reason)
you\'re welcome to send regular patches.

Be sure to also read the [Contributing to
Celery](https://docs.celeryq.dev/en/master/contributing.html) section in
the documentation.

[![oc-contributors](https://opencollective.com/celery/contributors.svg?width=890&button=false)](https://github.com/celery/celery/graphs/contributors)

## Backers

Thank you to all our backers! 🙏 \[[Become a
backer](https://opencollective.com/celery#backer)\]

[![oc-backers](https://opencollective.com/celery/backers.svg?width=890)](https://opencollective.com/celery#backers)

## Sponsors

Support this project by becoming a sponsor. Your logo will show up here
with a link to your website. \[[Become a
sponsor](https://opencollective.com/celery#sponsor)\]

[![oc-sponsors](https://opencollective.com/celery/sponsor/0/avatar.svg)](https://opencollective.com/celery/sponsor/0/website)

# License

This software is licensed under the [New BSD License]{.title-ref}. See
the `LICENSE` file in the top distribution directory for the full
license text.
