# I) URLS
### Desc


### Docs
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq

### Libs
https://github.com/rabbitmq
https://github.com/jbg/rabbitmq
https://github.com/celery/librabbitmq


# II) Description
RabbitMQ is feature-complete, stable, durable and easy to install. It’s an excellent choice for a production environment.


### Install
https://www.rabbitmq.com/download.html
```sh
sudo apt-get install rabbitmq-server
# or
docker run -d -p 5672:5672 rabbitmq
# When the command completes, the broker will already be running in the background, ready to move messages for you: Starting rabbitmq-server: SUCCESS.
nc -zv 127.0.0.1 5672  # check connection
```


# III) Usage
1) Case1
2) Case2

# IV) Pros
1) guarantees message delivery
2) fault-tolerant, supports synchronous replication, which allows for SSL to establish an encrypted connection
3) superb for real-time applications

# V) Cons
1) Bad1
2) Bad2

# VI) Compare
1) Diff1
2) Diff2
