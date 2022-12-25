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
* Email sending - You may want to send an email verification, a password reset email, or a confirmation of a form submission. Sending emails can take a while and slow down your app, especially if it has many users.
* Image processing - You might want to resize avatar images that users upload or apply some encoding on all images that users can share on your platform. Image processing is often a resource-intensive task that can slow down your web app, mainly if you’re serving a large community of users.
* Text processing: If you allow users to add data to your app, then you might want to monitor their input. For example, you may want to check for profanity in comments or translate user-submitted text to a different language. Handling all this work in the context of your web app can significantly impair performance.
* API calls and other web requests: If you need to make web requests to provide the service that your app offers, then you can quickly run into unexpected wait times. This is true for rate-limited API requests just as much as other tasks, such as web scraping. It’s often better to hand off these requests to a different process.
* Data analysis: Crunching data is notoriously resource-intensive. If your web app analyzes data for your users, you’ll quickly see your app become unresponsive if you’re handling all the work right within Django.
* Machine learning model runs: Just like with other data analysis, waiting for the results of machine learning operations can take a moment. Instead of letting your users wait for the calculations to complete, you can offload that work to Celery so they can continue browsing your web app until the results come back.
* Report generation: If you’re serving an app that allows users to generate reports from data they provided, you’ll notice that building PDF files doesn’t happen instantaneously. It’ll be a better user experience if you let Celery handle that in the background instead of freezing your web app until the report is ready for download.

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