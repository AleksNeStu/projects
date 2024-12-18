# Example using the Eventlet Pool

## Introduction

This is a Celery application containing two example tasks.

First you need to install Eventlet, and also recommended is the
[dnspython]{.title-ref} module (when this is installed all name lookups
will be asynchronous):

    $ python -m pip install eventlet celery pybloom-live

Before you run any of the example tasks you need to start the worker:

    $ cd examples/eventlet
    $ celery worker -l INFO --concurrency=500 --pool=eventlet

As usual you need to have RabbitMQ running, see the Celery getting
started guide if you haven\'t installed it yet.

## Tasks

- [tasks.urlopen]{.title-ref}

This task simply makes a request opening the URL and returns the size of
the response body:

    $ cd examples/eventlet
    $ python
    >>> from tasks import urlopen
    >>> urlopen.delay('https://www.google.com/').get()
    9980

To open several URLs at once you can do:

    $ cd examples/eventlet
    $ python
    >>> from tasks import urlopen
    >>> from celery import group
    >>> result = group(urlopen.s(url)
    ...                     for url in LIST_OF_URLS).apply_async()
    >>> for incoming_result in result.iter_native():
    ...     print(incoming_result)

- [webcrawler.crawl]{.title-ref}

This is a simple recursive web crawler. It will only crawl URLs for the
current host name. Please see comments in the
[webcrawler.py]{.title-ref} file.
