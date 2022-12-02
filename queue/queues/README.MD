# I) URLS


# II) Description
### Celery and RabbitMQ
Are some tools used in in event-driven architectures.

There is an increase in event-driven architectures as companies develop solutions that require asynchronous communication between their microservices.\
A task queue is a data structure maintained by a job scheduler containing jobs to run. Task queue software also manages background work that must be executed outside of the usual HTTP request-response cycle.\
They are designed for asynchronous operations, i.e, operations are executed in a non-blocking mode allowing the main operation to continue processing.\

### Type of tasks
*   Periodic tasks — Jobs that you will schedule to run at a specific time or after an interval, e.g., monthly report generation or a web scraper that runs twice a day.
* Third-party tasks — The web app must serve users quickly without waiting for other actions to complete while the page loads, e.g., sending an email or notification or propagating updates to internal tools (such as gathering data for A/B testing or system logging).
* Long-running jobs — Jobs that are expensive in resources, where users need to wait while they compute their results, e.g., complex workflow execution (DAG workflows), graph generation, Map-Reduce like tasks, and serving of media content (video, audio).

### Python 

A straightforward solution to execute a background task would be running it within a separate thread or process. Python threads, on the other hand, are coordinated and scheduled by the global interpreter lock ([GIL](https://wiki.python.org/moin/GlobalInterpreterLock)), which prevents multiple native threads from executing Python bytecodes at once.

### Review

**Designing communication between processes consistently is an error-prone process** and leads to code coupling and bad system maintainability, not to mention that it negatively affects scalability.

Python process is a normal process under an Operating System (OS) and, with the entire Python standard library, it becomes a heavyweight. As the number of processes in the app increases, switching from one such process to another becomes a time-consuming operation.


A much better solution is to serve a _distributed queue_ or its well-known sibling paradigm called _publish-subscribe_. As depicted in Figure 1, there are two types of applications in which one, called the _publisher_, sends messages and the other, called the _subscriber_, receives messages. Those two agents do not interact with each other directly and are not even aware of each other. Publishers send messages to a central queue, or _broker_, and subscribers receive messages of interest from this broker. There are two main advantages in this method:


-   Scalability — agents don’t need to know about each other in the network. They are focused by topic. So it means that each can continue to operate normally regardless of the other in asynchronous fashion.
-   Loose coupling — each agent represents its part of the system (service, module). Since they are loosely coupled, each can scale individually beyond the datacenter.


There are lots of messaging systems that support such paradigms and provide a neat API, driven either by TCP or HTTP protocols, e.g., JMS, RabbitMQ, Redis Pub/Sub, Apache ActiveMQ, etc.

![Publish-Subscribe paradigm with Celery Python](https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/191390/image-1582290828851-ca65ffad5d02f1456e5c208d2b00ba30.png)
Publish-Subscribe paradigm


### What's a Task Queue?

Task queues are used as a mechanism to distribute work across threads or machines.

A task queue's input is a unit of work, called a task, dedicated worker processes then constantly monitor the queue for new work to perform.

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker.