# I) URLS


# II) Description
### 1) multithreading
* A thread has access to the code, data and resources of its owner process (Care must be taken as to how threads access those resources).
* Thread synchronization primitives such as condition variables, semaphores, mutexes or barriers allow to control the way in which threads access shared resources
* A thread has its own stack, program counter and registers
* The program counter is a special register that tracks the instruction that is currently being executed (or the next instruction to be executed). When the scheduler switches between two threads running on a single CPU, a context switch takes place in which the state of the registers of the thread being switched from are stored and the registers of the thread being switched to are restored.
* thread creation is lightweight in comparison to spawning a new process.
* Critical section - refers to code that can result in a race condition when executed by multiple threads, because a a shared resource is involved.

### 2) multiprocessing
* **Processes do not share the same resources,** by default. Process synchronization, also known as Inter-Process Communication (IPC), must be used if resource sharing is necessary. Some of the most common mechanisms for achieving IPC are signals, sockets, message queues, pipes and shared memory.


### 3) asyncio

## - Parallelism
- is about doing lots of things at once.
- Whereas parallelism means that tasks are run on actually distinct CPUs.

## - Concurrency
- Concurrency is about dealing with lots of things at once.
- Concurrency is about structure.
- Concurrency provides a way to structure a solution to solve a problem that may (but not necessarily) be parallelizable.
- means that the operating system will schedule the tasks to run in an interleaved fashion, thus creating the illusion of them being executed at the same time.


### Race condition
A race condition leads to inconsistent results that stem from the order in which threads or processes act on some shared state.
Race conditions occur because access to the shared state happens outside of synchronization mechanisms
Occurs when several threads execute a critical section without synchronization mechanisms in place.
This problem can be solved by rendering critical sections atomic through thread synchronization primitives such as locks or semaphores.
### Deadlock
A deadlock occurs when several tasks are blocked indefinitely while holding a shared resource and while waiting for another one.
a) Mutual exclusion b) Hold and wait c) No preempt d) Circular wait
### Livelock
Unlike a deadlock, tasks in a livelock are overly polite: they acquire a resource, they test whether another resource is available, they release the first resource if the second one is not available, wait for a given amount of time, then repeat the whole process all over again. The irony is that livelocks often occur while attempting to correct for deadlocks…
### Starvation
Resource starvation occurs when a task never acquires a resource it needs
### Priority inversion occurs when a task with low priority holds a resource required by a task with high priority.



# III) Usage
1) 

# IV) Pros
1) 

# V) Cons
1) 

# VI) Compare
1) 
