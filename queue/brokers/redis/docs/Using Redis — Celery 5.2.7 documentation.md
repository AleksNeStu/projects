---
source: https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#broker-redis \
created: 2022-12-02T15:07:09 (UTC +01:00) \
tags: [] \
author: 
---
# Using Redis — Celery 5.2.7 documentation
---
This document describes the current stable version of Celery (5.2). For development docs, [go here](http://docs.celeryproject.org/en/master/getting-started/backends-and-brokers/redis.html).

## Installation[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#installation "Permalink to this headline")

For the Redis support you have to install additional dependencies. You can install both Celery and these dependencies in one go using the `celery[redis]` [bundle](https://docs.celeryq.dev/en/stable/getting-started/introduction.html#bundles):

```
$ pip install -U "celery[redis]"

```

## Configuration[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#configuration "Permalink to this headline")

Configuration is easy, just configure the location of your Redis database:

```
app.conf.broker_url = 'redis://localhost:6379/0'

```

Where the URL is in the format of:

```
redis://:password@hostname:port/db_number

```

all fields after the scheme are optional, and will default to `localhost` on port 6379, using database 0.

If a Unix socket connection should be used, the URL needs to be in the format:

```
redis+socket:///path/to/redis.sock

```

Specifying a different database number when using a Unix socket is possible by adding the `virtual_host` parameter to the URL:

```
redis+socket:///path/to/redis.sock?virtual_host=db_number

```

It is also easy to connect directly to a list of Redis Sentinel:

```
app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
app.conf.broker_transport_options = { 'master_name': "cluster1" }

```

Additional options can be passed to the Sentinel client using `sentinel_kwargs`:

```
app.conf.broker_transport_options = { 'sentinel_kwargs': { 'password': "password" } }

```

### Visibility Timeout[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#visibility-timeout "Permalink to this headline")

The visibility timeout defines the number of seconds to wait for the worker to acknowledge the task before the message is redelivered to another worker. Be sure to see [Caveats](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#redis-caveats) below.

This option is set via the [`broker_transport_options`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-broker_transport_options) setting:

```
app.conf.broker_transport_options = {'visibility_timeout': 3600}  # 1 hour.

```

The default visibility timeout for Redis is 1 hour.

### Results[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#results "Permalink to this headline")

If you also want to store the state and return values of tasks in Redis, you should configure these settings:

```
app.conf.result_backend = 'redis://localhost:6379/0'

```

For a complete list of options supported by the Redis result backend, see [Redis backend settings](https://docs.celeryq.dev/en/stable/userguide/configuration.html#conf-redis-result-backend).

If you are using Sentinel, you should specify the master\_name using the [`result_backend_transport_options`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-result_backend_transport_options) setting:

```
app.conf.result_backend_transport_options = {'master_name': "mymaster"}

```

#### Connection timeouts[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#connection-timeouts "Permalink to this headline")

To configure the connection timeouts for the Redis result backend, use the `retry_policy` key under [`result_backend_transport_options`](https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-result_backend_transport_options):

```
app.conf.result_backend_transport_options = {
    'retry_policy': {
       'timeout': 5.0
    }
}

```

See [`retry_over_time()`](https://docs.celeryq.dev/projects/kombu/en/master/reference/kombu.utils.functional.html#kombu.utils.functional.retry_over_time "(in Kombu v5.2)") for the possible retry policy options.

## Caveats[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#caveats "Permalink to this headline")

### Visibility timeout[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#id1 "Permalink to this headline")

If a task isn’t acknowledged within the [Visibility Timeout](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#redis-visibility-timeout) the task will be redelivered to another worker and executed.

This causes problems with ETA/countdown/retry tasks where the time to execute exceeds the visibility timeout; in fact if that happens it will be executed again, and again in a loop.

So you have to increase the visibility timeout to match the time of the longest ETA you’re planning to use.

Note that Celery will redeliver messages at worker shutdown, so having a long visibility timeout will only delay the redelivery of ‘lost’ tasks in the event of a power failure or forcefully terminated workers.

Periodic tasks won’t be affected by the visibility timeout, as this is a concept separate from ETA/countdown.

You can increase this timeout by configuring a transport option with the same name:

```
app.conf.broker_transport_options = {'visibility_timeout': 43200}

```

The value must be an int describing the number of seconds.

### Key eviction[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#key-eviction "Permalink to this headline")

Redis may evict keys from the database in some situations

If you experience an error like:

```
InconsistencyError: Probably the key ('_kombu.binding.celery') has been
removed from the Redis database.

```

then you may want to configure the **redis-server** to not evict keys by setting in the redis configuration file:

-   the `maxmemory` option
    
-   the `maxmemory-policy` option to `noeviction` or `allkeys-lru`
    

See Redis server documentation about Eviction Policies for details:

### Group result ordering[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#group-result-ordering "Permalink to this headline")

Versions of Celery up to and including 4.4.6 used an unsorted list to store result objects for groups in the Redis backend. This can cause those results to be be returned in a different order to their associated tasks in the original group instantiation. Celery 4.4.7 introduced an opt-in behaviour which fixes this issue and ensures that group results are returned in the same order the tasks were defined, matching the behaviour of other backends. In Celery 5.0 this behaviour was changed to be opt-out. The behaviour is controlled by the result\_chord\_ordered configuration option which may be set like so:

```
# Specifying this for workers running Celery 4.4.6 or earlier has no effect
app.conf.result_backend_transport_options = {
    'result_chord_ordered': True    # or False
}

```

This is an incompatible change in the runtime behaviour of workers sharing the same Redis backend for result storage, so all workers must follow either the new or old behaviour to avoid breakage. For clusters with some workers running Celery 4.4.6 or earlier, this means that workers running 4.4.7 need no special configuration and workers running 5.0 or later must have result\_chord\_ordered set to False. For clusters with no workers running 4.4.6 or earlier but some workers running 4.4.7, it is recommended that result\_chord\_ordered be set to True for all workers to ease future migration. Migration between behaviours will disrupt results currently held in the Redis backend and cause breakage if downstream tasks are run by migrated workers - plan accordingly.
