---
source: https://en.wikipedia.org/wiki/Structured_concurrency

created: 2023-10-24T23:29:37 (UTC +02:00)

tags: []

author: Contributors to Wikimedia projects

---
# Structured concurrency - Wikipedia
---
From Wikipedia, the free encyclopedia

**Structured concurrency** is a [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm "Programming paradigm") aimed at improving the clarity, quality, and development time of a [computer program](https://en.wikipedia.org/wiki/Computer_program "Computer program") by using a structured approach to [concurrent programming](https://en.wikipedia.org/wiki/Concurrent_computing "Concurrent computing").

The core concept is the encapsulation of concurrent threads of execution (here encompassing kernel and userland threads and processes) by way of control flow constructs that have clear entry and exit points and that ensure all spawned threads have completed before exit. Such encapsulation allows errors in concurrent threads to be propagated to the control structure's parent scope and managed by the native error handling mechanisms of each particular computer language. It allows control flow to remain readily evident by the structure of the source code despite the presence of concurrency. To be effective, this model must be applied consistently throughout all levels of the program – otherwise concurrent threads may leak out, become orphaned, or fail to have runtime errors correctly propagated.

Structured concurrency is analogous to [structured programming](https://en.wikipedia.org/wiki/Structured_programming "Structured programming"), which introduced control flow constructs that encapsulated sequential statements and subroutines.

## History\[[edit](https://en.wikipedia.org/w/index.php?title=Structured_concurrency&action=edit&section=1 "Edit section: History")\]

The [fork–join model](https://en.wikipedia.org/wiki/Fork%E2%80%93join_model "Fork–join model") from the 1960s, embodied by multiprocessing tools like [OpenMP](https://en.wikipedia.org/wiki/OpenMP "OpenMP"), is an early example of a system ensuring all threads have completed before exit. However, Smith argues that this model is not true structured concurrency as the programming language is unaware of the joining behavior, and is thus unable to enforce safety.<sup id="cite_ref-1"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-1">[1]</a></sup>

The concept was formulated in 2016 by Martin Sústrik (creator of [ZeroMQ](https://en.wikipedia.org/wiki/ZeroMQ "ZeroMQ")) with his C library libdill, with [goroutines](https://en.wikipedia.org/wiki/Go_(programming_language)#Concurrency:_goroutines_and_channels "Go (programming language)") as a starting point.<sup id="cite_ref-2"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-2">[2]</a></sup> It was further refined in 2017 by Nathaniel J. Smith, who introduced a "nursery pattern" in his [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python (programming language)") implementation called Trio.<sup id="cite_ref-3"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-3">[3]</a></sup> Meanwhile, Roman Elizarov independently came upon the same ideas while developing an experimental [coroutine](https://en.wikipedia.org/wiki/Coroutine "Coroutine") library for the [Kotlin language](https://en.wikipedia.org/wiki/Kotlin_(programming_language) "Kotlin (programming language)"),<sup id="cite_ref-4"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-4">[4]</a></sup><sup id="cite_ref-5"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-5">[5]</a></sup> which later became a standard library.<sup id="cite_ref-6"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-6">[6]</a></sup>

In 2021, [Swift](https://en.wikipedia.org/wiki/Swift_(programming_language) "Swift (programming language)") adopted structured concurrency.<sup id="cite_ref-7"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-7">[7]</a></sup> Later that year, a draft proposal was published to add structured concurrency to [Java](https://en.wikipedia.org/wiki/Java_(programming_language) "Java (programming language)").<sup id="cite_ref-8"><a href="https://en.wikipedia.org/wiki/Structured_concurrency#cite_note-8">[8]</a></sup>

## Variations\[[edit](https://en.wikipedia.org/w/index.php?title=Structured_concurrency&action=edit&section=2 "Edit section: Variations")\]

A major point of variation is how an error in one member of a concurrent thread tree is handled. Simple implementations will merely wait until the children and siblings of the failing thread run to completion before propagating the error to the parent scope. However, that could take an indefinite amount of time. The alternative is to employ a general cancellation mechanism (typically a cooperative scheme allowing program invariants to be honored) to terminate the children and sibling threads in an expedient manner.

## See also\[[edit](https://en.wikipedia.org/w/index.php?title=Structured_concurrency&action=edit&section=3 "Edit section: See also")\]

-   [Structured programming](https://en.wikipedia.org/wiki/Structured_programming "Structured programming")

## References\[[edit](https://en.wikipedia.org/w/index.php?title=Structured_concurrency&action=edit&section=4 "Edit section: References")\]

1.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-1 "Jump up")** Smith, Nathaniel J. (25 April 2018). ["Notes on structured concurrency, or: Go statement considered harmful"](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/). Retrieved 1 August 2019.
2.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-2 "Jump up")** Sústrik, Martin (7 February 2016). ["Structured Concurrency"](http://250bpm.com/blog:71). Retrieved 1 August 2019.
3.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-3 "Jump up")** Smith, Nathaniel J. (10 March 2017). ["Announcing Trio"](https://vorpus.org/blog/announcing-trio/). Retrieved 23 September 2022.
4.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-4 "Jump up")** Elizarov, Roman (12 September 2018). ["Structured concurrency"](https://medium.com/@elizarov/structured-concurrency-722d765aa952). Retrieved 21 September 2019.
5.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-5 "Jump up")** Elizarov, Roman (11 July 2019). [_Structured concurrency_](https://youtube.com/watch?v=Mj5P47F6nJg&t=2538) (Video). Hydra Distributed computing conference. 42 minutes in. Retrieved 21 September 2019. We needed a name and we needed to finalize this whole concept \[...\] and we stumble onto this blog post \[...\] by Nathaniel J. Smith.
6.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-6 "Jump up")** ["Coroutines basics: Structured concurrency"](https://kotlinlang.org/docs/coroutines-basics.html#structured-concurrency). _Kotlin_. JetBrains. Retrieved 3 March 2022.
7.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-7 "Jump up")** McCall, John; Groff, Joe; Gregor, Doug; Malawski, Konrad. ["Swift Structured Concurrency Proposal"](https://github.com/apple/swift-evolution/blob/main/proposals/0304-structured-concurrency.md). _Apple's Swift Evolution repo_. GitHub. Retrieved 3 March 2022.
8.  **[^](https://en.wikipedia.org/wiki/Structured_concurrency#cite_ref-8 "Jump up")** Pressler, Ron. ["JEP draft: Structured Concurrency (Incubator)"](https://openjdk.java.net/jeps/8277129). _[OpenJDK](https://en.wikipedia.org/wiki/OpenJDK "OpenJDK")_. Oracle. Retrieved 3 March 2022.

## External links\[[edit](https://en.wikipedia.org/w/index.php?title=Structured_concurrency&action=edit&section=5 "Edit section: External links")\]

-   [Notes on structured concurrency, or: Go statement considered harmful](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) by Nathaniel J. Smith
-   [Structured concurrency forum](https://trio.discourse.group/c/structured-concurrency), cross-computer-language discussion of structured concurrency with participation by Sústrik, Smith, and Elizarov
-   [FOSDEM 2019: Structured Concurrency](https://archive.fosdem.org/2019/schedule/event/structured_concurrency/), lightning talk by Martin Sustrik with links to some implementations
