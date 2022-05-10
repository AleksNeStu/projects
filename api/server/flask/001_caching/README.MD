# Info
Caching is the ability to store copies of frequently accessed data in several places along the request-response path. When a consumer requests a resource representation, the request goes through a cache or a series of caches (local cache, proxy cache, or reverse proxy) toward the service hosting the resource. If any of the caches along the request path has a fresh copy of the requested representation, it uses that copy to satisfy the request. If none of the caches can satisfy the request, the request travels to the service (or origin server as it is formally known). This is well defined with two terminologies, which are cache miss and cache hit.

Cache hit — A cache hit is a state in which data requested for processing by a component or application is found in the cache memory.

Cache miss — Cache miss is a state where the data requested for processing by a component or application is not found in the cache memory.

That can be on the:
1) client-side through Web Caching
2) server-side through\
a) Data Caching (Relational Databases, Redis, etc)\
b) Application Caching through plugins that get installed on the application (ex: plugins on WordPress).


# Task
We have two endpoints which contains posts and comments belonging to these posts.

We want to create a small caching microservice in front of these endpoints, which are combining the comments and posts into logical units.

https://jsonplaceholder.typicode.com/posts

https://jsonplaceholder.typicode.com/comments


# Docker
``sh
docker-compose up -d --build
``