---
source: https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#broker-overview \
created: 2022-12-02T15:32:08 (UTC +01:00) \
tags: [] \
author: 
---
# Backends and Brokers — Celery 5.2.7 documentation
---
This document describes the current stable version of Celery (5.2). For development docs, [go here](http://docs.celeryproject.org/en/master/getting-started/backends-and-brokers/index.html).

Release

5.2

Date

May 29, 2022

Celery supports several message transport alternatives.

## Broker Overview[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#broker-overview "Permalink to this headline")

This is comparison table of the different transports supports, more information can be found in the documentation for each individual transport (see [Broker Instructions](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#broker-toc)).

<table><colgroup><col> <col> <col> <col></colgroup><tbody><tr><td><p><strong>Name</strong></p></td><td><p><strong>Status</strong></p></td><td><p><strong>Monitoring</strong></p></td><td><p><strong>Remote Control</strong></p></td></tr><tr><td><p><em>RabbitMQ</em></p></td><td><p>Stable</p></td><td><p>Yes</p></td><td><p>Yes</p></td></tr><tr><td><p><em>Redis</em></p></td><td><p>Stable</p></td><td><p>Yes</p></td><td><p>Yes</p></td></tr><tr><td><p><em>Amazon SQS</em></p></td><td><p>Stable</p></td><td><p>No</p></td><td><p>No</p></td></tr><tr><td><p><em>Zookeeper</em></p></td><td><p>Experimental</p></td><td><p>No</p></td><td><p>No</p></td></tr></tbody></table>

Experimental brokers may be functional but they don’t have dedicated maintainers.

Missing monitor support means that the transport doesn’t implement events, and as such Flower, celery events, celerymon and other event-based monitoring tools won’t work.

Remote control means the ability to inspect and manage workers at runtime using the celery inspect and celery control commands (and other tools using the remote control API).

## Summaries[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#summaries "Permalink to this headline")

_Note: This section is not comprehensive of backends and brokers._

Celery has the ability to communicate and store with many different backends (Result Stores) and brokers (Message Transports).

### Redis[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#redis "Permalink to this headline")

Redis can be both a backend and a broker.

**As a Broker:** Redis works well for rapid transport of small messages. Large messages can congest the system.

[See documentation for details](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#broker-redis)

**As a Backend:** Redis is a super fast K/V store, making it very efficient for fetching the results of a task call. As with the design of Redis, you do have to consider the limit memory available to store your data, and how you handle data persistence. If result persistence is important, consider using another DB for your backend.

### RabbitMQ[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#rabbitmq "Permalink to this headline")

RabbitMQ is a broker.

**As a Broker:** RabbitMQ handles larger messages better than Redis, however if many messages are coming in very quickly, scaling can become a concern and Redis or SQS should be considered unless RabbitMQ is running at very large scale.

[See documentation for details](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq)

**As a Backend:** RabbitMQ can store results via `rpc://` backend. This backend creates separate temporary queue for each client.

_Note: RabbitMQ (as the broker) and Redis (as the backend) are very commonly used together. If more guaranteed long-term persistence is needed from the result store, consider using PostgreSQL or MySQL (through SQLAlchemy), Cassandra, or a custom defined backend._

### SQS[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#sqs "Permalink to this headline")

SQS is a broker.

If you already integrate tightly with AWS, and are familiar with SQS, it presents a great option as a broker. It is extremely scalable and completely managed, and manages task delegation similarly to RabbitMQ. It does lack some of the features of the RabbitMQ broker such as `worker remote control commands`.

[See documentation for details](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/sqs.html#broker-sqs)

### SQLAlchemy[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#sqlalchemy "Permalink to this headline")

SQLAlchemy is backend.

It allows Celery to interface with MySQL, PostgreSQL, SQlite, and more. It is a ORM, and is the way Celery can use a SQL DB as a result backend. Historically, SQLAlchemy has not been the most stable result backend so if chosen one should proceed with caution.
