---
source: https://sniffio.readthedocs.io/en/latest/

created: 2023-10-26T14:06:11 (UTC +02:00)

tags: []

author: 

---
# sniffio: Sniff out which async library your code is running under — sniffio 1.3.0+dev documentation
---
[sniffio](https://sniffio.readthedocs.io/en/latest/#)

You’re writing a library. You’ve decided to be ambitious, and support multiple async I/O packages, like [Trio](https://trio.readthedocs.io/), and [asyncio](https://docs.python.org/3/library/asyncio.html), and … You’ve written a bunch of clever code to handle all the differences. But… how do you know _which_ piece of clever code to run?

This is a tiny package whose only purpose is to let you detect which async library your code is running under.

-   Documentation: [https://sniffio.readthedocs.io](https://sniffio.readthedocs.io/)
-   Bug tracker and source code: [https://github.com/python-trio/sniffio](https://github.com/python-trio/sniffio)
-   License: MIT or Apache License 2.0, your choice
-   Contributor guide: [https://trio.readthedocs.io/en/latest/contributing.html](https://trio.readthedocs.io/en/latest/contributing.html)
-   Code of conduct: Contributors are requested to follow our [code of conduct](https://trio.readthedocs.io/en/latest/code-of-conduct.html) in all project spaces.

This library is maintained by the Trio project, as a service to the async Python community as a whole.

## Usage[¶](https://sniffio.readthedocs.io/en/latest/#usage "Permalink to this headline")

`sniffio.``current_async_library`() → str[¶](https://sniffio.readthedocs.io/en/latest/#sniffio.current_async_library "Permalink to this definition")

Detect which async library is currently running.

The following libraries are currently supported:

  
| Library | Requires | Magic string |
| --- | --- | --- |
| **Trio** | Trio v0.6+ | `"trio"` |
| **Curio** | 
 | `"curio"` |
| **asyncio** |   | `"asyncio"` |
| **Trio-asyncio** | v0.8.2+ | `"trio"` or `"asyncio"`, depending on current mode |

<table><colgroup><col> <col></colgroup><tbody><tr><th>Returns:</th><td>A string like <code><span>"trio"</span></code>.</td></tr><tr><th>Raises:</th><td><a href="https://sniffio.readthedocs.io/en/latest/#sniffio.AsyncLibraryNotFoundError" title="sniffio.AsyncLibraryNotFoundError"><code><span>AsyncLibraryNotFoundError</span></code></a> – if called from synchronous context, or if the current async library was not recognized.</td></tr></tbody></table>

Examples

```
from sniffio import current_async_library

async def generic_sleep(seconds):
    library = current_async_library()
    if library == "trio":
        import trio
        await trio.sleep(seconds)
    elif library == "asyncio":
        import asyncio
        await asyncio.sleep(seconds)
    # ... and so on ...
    else:
        raise RuntimeError(f"Unsupported library {library!r}")

```

_exception_ `sniffio.``AsyncLibraryNotFoundError`[¶](https://sniffio.readthedocs.io/en/latest/#sniffio.AsyncLibraryNotFoundError "Permalink to this definition")

## Adding support to a new async library[¶](https://sniffio.readthedocs.io/en/latest/#adding-support-to-a-new-async-library "Permalink to this headline")

If you’d like your library to be detected by `sniffio`, it’s pretty easy.

**Step 1:** Pick the magic string that will identify your library. To avoid collisions, this should match your library’s PEP 503 normalized name on PyPI.

**Step 2:** There’s a special [`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "(in Python v3.10)") object:

`thread_local.``name`[¶](https://sniffio.readthedocs.io/en/latest/#sniffio.thread_local.name "Permalink to this definition")

Make sure that whenever your library is calling a coroutine `throw()`, `send()`, or `close()` that this is set to your identifier string. In most cases, this will be as simple as:

```
from sniffio import thread_local

# Your library's step function
def step(...):
     old_name, thread_local.name = thread_local.name, "my-library's-PyPI-name"
     try:
         result = coro.send(None)
     finally:
         thread_local.name = old_name

```

**Step 3:** Send us a PR to add your library to the list of supported libraries above.

That’s it!

There are libraries that directly drive a sniffio-naive coroutine from another, outer sniffio-aware coroutine such as trio\_asyncio. These libraries should make sure to set the correct value while calling a synchronous function that will go on to drive the sniffio-naive coroutine.

```
from sniffio import thread_local

# Your library's compatibility loop
async def main_loop(self, ...) -> None:
     ...
     handle: asyncio.Handle = await self.get_next_handle()
     old_name, thread_local.name = thread_local.name, "asyncio"
     try:
         result = handle._callback(obj._args)
     finally:
         thread_local.name = old_name

```

-   [Release history](https://sniffio.readthedocs.io/en/latest/history.html)
