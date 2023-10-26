[![Join chatroom](https://img.shields.io/badge/chat-join%20now-blue.svg)](https://gitter.im/python-trio/general)

[![Join forum](https://img.shields.io/badge/forum-join%20now-blue.svg)](https://trio.discourse.group)

[![Documentation](https://img.shields.io/badge/docs-read%20now-blue.svg)](https://trio.readthedocs.io)

[![Latest PyPi version](https://img.shields.io/pypi/v/trio.svg)](https://pypi.org/project/trio)

[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/trio.svg)](https://anaconda.org/conda-forge/trio)

[![Test coverage](https://codecov.io/gh/python-trio/trio/branch/master/graph/badge.svg)](https://codecov.io/gh/python-trio/trio)

# Trio -- a friendly Python library for async concurrency and I/O

![image](https://raw.githubusercontent.com/python-trio/trio/9b0bec646a31e0d0f67b8b6ecc6939726faf3e17/logo/logo-with-background.svg){.align-right
width="200px"}

The Trio project aims to produce a production-quality, [permissively
licensed](https://github.com/python-trio/trio/blob/master/LICENSE),
async/await-native I/O library for Python. Like all async libraries, its
main purpose is to help you write programs that do **multiple things at
the same time** with **parallelized I/O**. A web spider that wants to
fetch lots of pages in parallel, a web server that needs to juggle lots
of downloads and websocket connections simultaneously, a process
supervisor monitoring multiple subprocesses\... that sort of thing.
Compared to other libraries, Trio attempts to distinguish itself with an
obsessive focus on **usability** and **correctness**. Concurrency is
complicated; we try to make it *easy* to get things *right*.

Trio was built from the ground up to take advantage of the [latest
Python features](https://www.python.org/dev/peps/pep-0492/), and draws
inspiration from [many
sources](https://github.com/python-trio/trio/wiki/Reading-list), in
particular Dave Beazley\'s [Curio](https://curio.readthedocs.io/). The
resulting design is radically simpler than older competitors like
[asyncio](https://docs.python.org/3/library/asyncio.html) and
[Twisted](https://twistedmatrix.com/), yet just as capable. Trio is the
Python I/O library I always wanted; I find it makes building
I/O-oriented programs easier, less error-prone, and just plain more fun.
[Perhaps you\'ll find the
same](https://github.com/python-trio/trio/wiki/Testimonials).

This project is young and still somewhat experimental: the overall
design is solid, and the existing features are fully tested and
documented, but you may encounter missing functionality or rough edges.
We *do* encourage you to use it, but you should [read and subscribe to
issue #1](https://github.com/python-trio/trio/issues/1) to get a warning
and a chance to give feedback about any compatibility-breaking changes.

## Where to next?

**I want to try it out!** Awesome! We have a [friendly
tutorial](https://trio.readthedocs.io/en/stable/tutorial.html) to get
you started; no prior experience with async coding is required.

**Ugh, I don\'t want to read all that -- show me some code!** If you\'re
impatient, then here\'s a [simple concurrency
example](https://trio.readthedocs.io/en/stable/tutorial.html#tutorial-example-tasks-intro),
an [echo
client](https://trio.readthedocs.io/en/stable/tutorial.html#tutorial-echo-client-example),
and an [echo
server](https://trio.readthedocs.io/en/stable/tutorial.html#tutorial-echo-server-example).

**How does Trio make programs easier to read and reason about than
competing approaches?** Trio is based on a new way of thinking that we
call \"structured concurrency\". The best theoretical introduction is
the article [Notes on structured concurrency, or: Go statement
considered
harmful](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/).
Or, [check out this talk at PyCon
2018](https://www.youtube.com/watch?v=oLkfnc_UMcE) to see a
demonstration of implementing the \"Happy Eyeballs\" algorithm in an
older library versus Trio.

**Cool, but will it work on my system?** Probably! As long as you have
some kind of Python 3.8-or-better (CPython or \[currently maintained
versions of
PyPy3\](<https://doc.pypy.org/en/latest/faq.html#which-python-versions-does-pypy-implement>)
are both fine), and are using Linux, macOS, Windows, or FreeBSD, then
Trio will work. Other environments might work too, but those are the
ones we test on. And all of our dependencies are pure Python, except for
CFFI on Windows, which has wheels available, so installation should be
easy (no C compiler needed).

**I tried it, but it\'s not working.** Sorry to hear that! You can try
asking for help in our [chat
room](https://gitter.im/python-trio/general) or
[forum](https://trio.discourse.group), [filing a
bug](https://github.com/python-trio/trio/issues/new), or [posting a
question on
StackOverflow](https://stackoverflow.com/questions/ask?tags=python+python-trio),
and we\'ll do our best to help you out.

**Trio is awesome, and I want to help make it more awesome!** You\'re
the best! There\'s tons of work to do -- filling in missing
functionality, building up an ecosystem of Trio-using libraries,
usability testing (e.g., maybe try teaching yourself or a friend to use
Trio and make a list of every error message you hit and place where you
got confused?), improving the docs, \... check out our [guide for
contributors](https://trio.readthedocs.io/en/stable/contributing.html)!

**I don\'t have any immediate plans to use it, but I love geeking out
about I/O library design!** That\'s a little weird? But let\'s be
honest, you\'ll fit in great around here. We have a [whole sub-forum for
discussing structured
concurrency](https://trio.discourse.group/c/structured-concurrency)
(developers of other systems welcome!). Or check out our [discussion of
design
choices](https://trio.readthedocs.io/en/stable/design.html#user-level-api-principles),
[reading list](https://github.com/python-trio/trio/wiki/Reading-list),
and [issues tagged
design-discussion](https://github.com/python-trio/trio/labels/design%20discussion).

**I want to make sure my company\'s lawyers won\'t get angry at me!** No
worries, Trio is permissively licensed under your choice of MIT or
Apache 2. See
[LICENSE](https://github.com/python-trio/trio/blob/master/LICENSE) for
details.

## Code of conduct

Contributors are requested to follow our [code of
conduct](https://trio.readthedocs.io/en/stable/code-of-conduct.html) in
all project spaces.