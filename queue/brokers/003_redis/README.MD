# I) URLS
### Desc


### Docs
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#broker-redis

### Libs


# II) Description
Redis is also feature-complete, but is more susceptible to data loss in the event of abrupt termination or power failures

### Install
```sh
docker run -d -p 6379:6379 redis
```

# III) Usage
1) Case1
2) Case2

# IV) Pros
1) Good1
2) Good2

# V) Cons
1) doesn’t support automatic replication
2) is manual and requires extra work to turn it into a message broker
3) memory-based. If the machine runs out of memory when building queues up, there’s a chance of losing tasks
4) SSL option is part of the paid version

# VI) Compare
1) Diff1
2) Diff2
