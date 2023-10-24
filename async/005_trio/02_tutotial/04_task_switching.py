import trio


async def child1():
    print("  child1: started! sleeping now...")
    await trio.sleep(1)
    print("  child1: exiting!")
    return 1

async def child2():
    print("  child2: started! sleeping now...")
    await trio.sleep(2)
    print("  child2: exiting!")
    return 2


async def parent():
    print("parent: started!")
    async with trio.open_nursery() as nursery:
        print("parent: spawning child1...")
        nursery.start_soon(child1)

        print("parent: spawning child2...")
        nursery.start_soon(child2)

        print("parent: waiting for children to finish...")
        # -- we exit the nursery block


"""
We want to watch trio.run() at work, which we can do by writing a class we’ll call Tracer, which implements Trio’s
Instrument interface. Its job is to log various events as they happen.
"""

class Tracer(trio.abc.Instrument):
    """The interface for run loop instrumentation.

    Instruments don't have to inherit from this abstract base class, and all
    of these methods are optional. This class serves mostly as documentation.

    """

    def before_run(self):
        print("!!! run started")

    def _print_with_task(self, msg, task):
        # repr(task) is perhaps more useful than task.name in general,
        # but in context of a tutorial the extra noise is unhelpful.
        print(f"{msg}: {task.name}")

    def task_spawned(self, task):
        self._print_with_task("### new task spawned", task)

    def task_scheduled(self, task):
        self._print_with_task("### task scheduled", task)

    def before_task_step(self, task):
        self._print_with_task(">>> about to run one step of task", task)

    def after_task_step(self, task):
        self._print_with_task("<<< task step finished", task)

    def task_exited(self, task):
        self._print_with_task("### task exited", task)

    def before_io_wait(self, timeout):
        if timeout:
            print(f"### waiting for I/O for up to {timeout} seconds")
        else:
            print("### doing a quick check for I/O")
        self._sleep_time = trio.current_time()

    def after_io_wait(self, timeout):
        duration = trio.current_time() - self._sleep_time
        print(f"### finished I/O check (took {duration} seconds)")

    def after_run(self):
        print("!!! run finished")


trio.run(parent, instruments=[Tracer()])

"""
in the middle you can see that Trio has created a task for the __main__.parent function, and “scheduled” it (i.e., 
made a note that it should be run soon).
Each task runs until it hits the call to trio.sleep(), and then suddenly we’re back in trio.run() deciding what to run next. How does this happen? The secret is that trio.run() and trio.sleep() work together to make it happen: trio.sleep() has access to some special magic that lets it pause itself, so it sends a note to trio.run() requesting to be woken again after 1 second, and then suspends the task. 
 And once the task is suspended, Python gives control back to trio.run(), which decides what to do next. (If this sounds similar to the way that generators can suspend execution by doing a yield

yield, then that’s not a coincidence: inside the Python interpreter, there’s a lot of overlap between the implementation of generators and async functions.)


You might wonder whether you can mix-and-match primitives from different async libraries. For example, could we use trio.run() together with asyncio.sleep()? The answer is no, we can’t, and the paragraph above explains why: the two sides of our async sandwich have a private language they use to talk to each other, and different libraries use different languages. So if you try to call asyncio.sleep() from inside a trio.run(), then Trio will get very confused indeed and probably blow up in some dramatic way.

That was a lot of text, but again, you don’t need to understand everything here to use Trio – in fact, Trio goes to great lengths to make each task feel like it executes in a simple, linear way. (Just like your operating system goes to great lengths to make it feel like your single-threaded code executes in a simple linear way, even though under the covers the operating system juggles between different threads and processes in essentially the same way Trio does.) But it is useful to have a rough model in your head of how the code you write is actually executed, and – most importantly – the consequences of that for parallelism.

Alternatively, if this has just whetted your appetite and you want to know more about how async/await works internally, then this blog post is a good deep dive, or check out this great walkthrough to see how to build a simple async I/O framework from the ground up.
"""