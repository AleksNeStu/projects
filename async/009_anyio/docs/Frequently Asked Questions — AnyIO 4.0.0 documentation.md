---
source: https://anyio.readthedocs.io/en/stable/faq.html

created: 2023-10-28T19:52:38 (UTC +02:00)

tags: []

author: 

---
# Frequently Asked Questions — AnyIO 4.0.0 documentation
---
## Why is Curio not supported as a backend?[¶](https://anyio.readthedocs.io/en/stable/faq.html#why-is-curio-not-supported-as-a-backend "Link to this heading")

[Curio](https://github.com/dabeaz/curio) was supported in AnyIO before v3.0. Support for it was dropped for two reasons:

1.  Its interface allowed only coroutine functions to access the [Curio](https://github.com/dabeaz/curio) kernel. This forced AnyIO to follow suit in its own API design, making it difficult to adapt existing applications that relied on synchronous callbacks to use AnyIO. It also interfered with the goal of matching Trio’s API in functions with the same purpose (e.g. `Event.set()`).
    
2.  The maintainer specifically requested [Curio](https://github.com/dabeaz/curio) support to be removed from AnyIO ([issue 185](https://github.com/agronholm/anyio/issues/185)).
    

## Why is Twisted not supported as a backend?[¶](https://anyio.readthedocs.io/en/stable/faq.html#why-is-twisted-not-supported-as-a-backend "Link to this heading")

The minimum requirement to support [Twisted](https://twistedmatrix.com/trac/) would be for [sniffio](https://github.com/python-trio/sniffio) to be able to detect a running Twisted event loop (and be able to tell when [Twisted](https://twistedmatrix.com/trac/) is being run on top of its asyncio reactor). This is not currently supported in [sniffio](https://github.com/python-trio/sniffio), so AnyIO cannot support Twisted either.

There is a Twisted [issue](https://github.com/twisted/twisted/pull/1263) that you can follow if you’re interested in Twisted support in AnyIO.
