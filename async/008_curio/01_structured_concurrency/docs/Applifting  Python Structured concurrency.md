---
source: https://applifting.io/blog/python-structured-concurrency

created: 2023-10-24T16:11:52 (UTC +02:00)

tags: []

author: 

---
# Applifting | Python: Structured concurrency
---
By

Jan Plesnik

|

25.10.2022

![](https://applifting.io/_next/image?url=https%3A%2F%2Fimages.prismic.io%2Fapplifting-website%2F7bfd757a-8a4d-48a4-883c-075488ce19de_Structured%2Bconcurrency%2Bin%2BPython%2B-%2Bu%25CC%2581vodni%25CC%2581%2B%25281%2529.jpg%3Fauto%3Dcompress%2Cformat&w=3840&q=75)

With the adoption of async-await syntax, modern Python has seen an emergence of coroutine-based asynchronous programming. Frameworks such as the standard library [asyncio](https://docs.python.org/3/library/asyncio.html), [Trio](https://github.com/python-trio/trio), and Dave Beazley's [Curio](https://github.com/dabeaz/curio) provide event loop implementations and high-level APIs for running coroutines, spawning tasks, and synchronizing between them. Nowadays, many see async Python as the de-facto standard approach to writing high-performance network-bound code, such as web servers and database interface libraries. This includes us at Applifting, and since sharing know-how is part of our culture, we are always eager to talk about our experience and practices. In this article, we will discuss the upcoming addition of task groups to Python’s asyncio and how they help us write resilient and maintainable concurrent code at scale.

## Signull case study

At Applifting, we have chosen Python to develop the backend for [Signull](https://www.signull.io/), a cryptocurrency market analysis tool for powertraders. The project faced a number of technical challenges. In the initial phases, the product team was navigating the uncharted and ever-changing crypto domain and looking to shape an MVP for user validation. Developers needed to make swift deliveries and continuously iterate on new ideas, making it difficult to lay a solid architectural foundation. We were experimenting with various data sources, designing and deprecating worker services on a weekly basis, and looking for ways to ingest live price data for tens of thousands of instruments with minimal latency. The network-bound nature of most technical problems made Python an attractive choice; the concurrency model adopted by asyncio fit the bill nicely.

Signull’s data ingress operates at the scale of hundreds of HTTP requests per second, all the while retrying failed requests, respecting variable rate limits, and synchronizing responses with data fed over not-always-reliable websocket connections. Some workers operate in multiple replicas to facilitate the rate of ingestion, depending on Redis and RabbitMQ for synchronization. As the system scaled, we realized that the product's success will depend on sound usage of synchronization mechanisms, re-entrancy, and resilience in face of network issues and unreliable data providers.

We learned many valuable lessons on this journey. One of them is that concurrency at scale desperately needs—yet often lacks—strict and enforceable structure. Before we dive into the details of what this means in practice, let us recapitulate on Python’s concurrency model.

## Coroutine-based concurrency

Coroutines can be understood as an alternative concurrency model to shared-state threading (whether system native or [not](https://en.wikipedia.org/wiki/Green_thread)). In the Python community, the threading module is often dismissed as inadequate or even pointless due to the notorious CPython GIL (although there are [valid reasons for its existence](https://www.youtube.com/watch?v=KVKufdTphKs&t=731s)). GIL aside, however, multithreading as an implementation-agnostic concept is still burdened by a number of issues. In a system with preemptive scheduling and arbitrary concurrent execution, local reasoning becomes significantly more difficult and error prone. Developers must introduce mutex and synchronization mechanisms to protect against race conditions, but the correctness of such mitigations is difficult to verify and must be considered whenever making adjustments to the code or even calling it.

_You have to have a level of vigilance bordering on paranoia just to make sure that your conventions around where state can be manipulated and by whom are honoured, because when such an interaction causes a bug it’s nearly impossible to tell where it came from._

-   [_Glyph, Unyielding_](https://blog.glyph.im/2014/02/unyielding.html)

Coroutines differ from threads in that they implement cooperative multitasking—they must yield control or suspend explicitly (e.g. via a yield or await statement). This means that the programmer is always aware of a potential context switch and is able to arrange a graceful and safe suspension. Glyph [compares](https://blog.glyph.im/2014/02/unyielding.html) this sort of statement to a relief valve: a single clearly marked point where we have to consider the implications of a potential transfer of control. As such, coroutines can be thought of as semantic improvement over threads.

## The problem of runaway tasks

Despite the convenience of coroutine-based concurrency, Python's asyncio module has long lacked an intuitive and convenient way to manage groups of concurrently running tasks. The current API revolves around [_create\_task_](https://docs.python.org/3.11/library/asyncio-task.html#asyncio.create_task), which returns a task handle to the user. The user is then responsible for keeping references to running tasks, collecting return values, and handling safe cancellation in case of errors. This is notoriously difficult and prone to errors. The lack of correct task management leads to runaway tasks, which never get awaited by the parent or checked for exceptions. As a result, the program can easily end up in an invalid state while failing to emit any kind of error or warning.

Consider the following code:

![](https://images.prismic.io/applifting-website/c45428ae-6f7d-41c7-b1fa-d9f2c1caaf51_Structured+concurrency+in+Python-obr-IV+%281%29.jpg?auto=compress,format)

The parent task spawns two child tasks, **A** and **B**, and lets them run in the background. Eventually, it awaits the completion of **A**. Once **A** is done, it either produces a return value or propagates an exception into the call stack. However, **B** is never awaited, which is not strictly wrong, but it exposes us to the following scenarios:

-   The task dies without our knowledge. Seemingly unrelated code may deadlock or start misbehaving, as it assumes that the task is running in the background.
-   We expect the task to have ended, but a bug in its termination logic makes it run silently in the background, causing unexpected behavior elsewhere.

Both situations are nightmares to debug. Once the example function exits, **B** becomes orphaned—we lose our reference to the task and are no longer able to manage its lifetime.

The control flow can be illustrated as such:

![](https://images.prismic.io/applifting-website/70b32a87-e6e3-4520-80f8-c10a3423bb38_Structured+concurrency+in+Python-diagram-II+%281%29.jpg?auto=compress,format)

While task **A** eventually rejoins the parent, task **B** runs away, and we lose control over it. It is possible to make an analogy to an orphan thread. The issue at hand is that asyncio not only doesn't help us prevent such behaviors, it almost hints at them being the correct and safe approach to concurrent computation.

What can be done to alleviate this problem?

## Enter nurseries

Let's look at the approach taken by Trio, an alternative async Python framework. In Trio, it is not possible to spawn tasks without first giving them a place to live: a nursery. Nurseries are context managers that expose an interface similar to _asyncio.create\_task_. However, tasks are always owned and managed by the nursery which spawned them, and the nursery context will never exit until all its tasks have completed by producing a return value or raising an exception. When a task fails, the nursery ensures that all concurrently running tasks are properly canceled, giving every task the ability to gracefully clean up. After all tasks are done, the exception is propagated back through the call stack.

Let's look at an example:

![](https://images.prismic.io/applifting-website/2b992d0e-f2da-44a6-950e-f05c08e4387f_Structured+concurrency+in+Python-obr-III+%281%29.jpg?auto=compress,format)

Trio ensures that the _async with_ block will not exit until both tasks have completed. Arbitrary computation, including await statements, can be done before, in-between, and after task creation. To aid with this, nurseries also offer a blocking [_start_](https://trio.readthedocs.io/en/stable/reference-core.html#trio.Nursery.start) call, which allows waiting for a task to initialize but not finish. For example, we may want to wait for a consumer task to establish connection to a message broker before proceeding with a corresponding producer task. Arbitrary nesting is allowed—tasks can open their own nurseries internally, which creates a hierarchical structure with clearly defined parent-child relationships. To retrieve return values from tasks, it is common to use a shared object, such as an async-ready queue or a plain dictionary. In many cases, however, tasks primarily need to pass information between one another, which is commonly achieved by passing a shared queue reference, as seen in the example.

Nurseries serve as explicit branching points, where the lifetime of concurrent tasks begins and eventually ends. One of the advantages of this pattern is that every task has a parent awaiting its completion. This guarantees that exceptions happening in concurrent tasks always have a place to propagate to. The control flow diagram now looks like this:

![](https://images.prismic.io/applifting-website/d0eb0a86-a429-4dce-9d5c-5ccea894fd02_Structured+concurrency+in+Python-diagram-I+%281%29.jpg?auto=compress,format)

We have previously discussed how coroutines make reasoning about concurrency easier due to explicit suspension points. Similarly, the nursery pattern creates semantic improvement via explicit lifetime representation of async tasks. This relatively new concept is often referred to as **structured concurrency** and is explained in great detail in Martin Sústrik’s [blog post](https://250bpm.com/blog:71/). Surveying other modern languages, we can draw a clear parallel to [Kotlin’s coroutine library](https://kotlinlang.org/docs/coroutines-basics.html#structured-concurrency), which achieves structured concurrency via [CoroutineScope](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/). Its purpose is analogous to Trio’s nurseries: to delimit the lifetime of concurrent tasks, ensure that they never leak, and never swallow errors silently. A [nursery implementation also exists for Golang](https://github.com/arunsworld/nursery), but it is not part of the standard library.

The observed benefits of structured concurrency can be compared to those of the now commonplace [structured programming](https://en.wikipedia.org/wiki/Structured_programming). Enforcing a logical structure on a program’s control flow makes it easier to understand, modify, and verify for correctness.

## Nurseries in asyncio

Now, let us return to the world of Python, where the majority of async libraries—and therefore applications using them—only aim for asyncio compatibility. One may rightfully question the practicality of Trio’s nurseries in such an ecosystem, apart from a theoretical proof of concept. Fortunately, the amazing [AnyIO project](https://anyio.readthedocs.io/en/stable/) implements structured concurrency on top of asyncio, making it available for widespread use. In AnyIO, nurseries are generalized as task groups. Additionally, AnyIO implements exception groups (analogous to Trio's _MultiError_), which serve as an abstraction over a number of exceptions raised in concurrently executing tasks. AnyIO claims compatibility with Python 3.6.2 and above, allowing us to introduce structure to existing codebases.

Most importantly, however, task groups are soon becoming native to Python's asyncio with the upcoming 3.11 release. This is supported by [PEP 654](https://peps.python.org/pep-0654/), which syntactically extends except clauses and makes exception groups a feature of the language itself. CPython core developer Yury Selivanov believes that "[this makes Python one of the best-equipped languages for writing concurrent code.](https://twitter.com/1st1/status/1493748850472873991)" Task groups effectively replace _asyncio.gather_, providing an all-around better API for concurrent task execution. The presence of task groups in the standard library is not only convenient for seasoned developers, but it also leads beginners to better practices and patterns that ultimately result in safer, better code.

## Conclusion

Throughout Python’s long history, we have seen an emergence of various frameworks implementing coroutine-based concurrency. The standard library has provided futures and executors, and eventually asyncio and async-await syntax. Meanwhile, many community projects developed in parallel, such as StacklessPython, Twisted, Gevent, or Tornado. For a long time, concurrency in Python has been in a fragmented state and lacked broader consensus on standard tooling and approaches. Given this historic context, it is fantastic to see the language’s ecosystem not only stabilize around asyncio but also become one of the first to implement—and help refine—modern patterns and paradigms.

Applifting’s Python team can speak from experience. Task groups allowed us to gradually introduce structure to Signull’s heavily concurrent codebase, drastically improving our ability to reason about it. In turn, we started designing and delivering safer and more resilient solutions. This led to a noticeable improvement in our productivity and the availability of our services. We were able to extort annoying [heisenbugs](https://en.wikipedia.org/wiki/Heisenbug), improve our error reporting, and allow services to gracefully recover in unexpected scenarios. It is in the [Zen of Python](https://peps.python.org/pep-0020/) that errors should never pass silently, and task groups finally give us a powerful tool to ensure this principle despite the intricacies of concurrent computation.

Did you get lost? [Simply reach out](https://applifting.cz/contact) and our experienced team will be happy to assist you.

## Join our newsletter

By clicking the button I agree with the collection and processing of my personal data as described in the [Privacy policy](https://applifting.io/privacy_policy_appilfting.pdf).
