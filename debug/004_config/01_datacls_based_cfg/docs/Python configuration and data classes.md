---
source: https://alexandra-zaharia.github.io/posts/python-configuration-and-dataclasses/ \
created: 2022-12-26T23:27:57 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Python configuration and data classes | Alexandra Zaharia
---
I stumbled upon an interesting [article](https://tech.preferred.jp/en/blog/working-with-configuration-in-python/) in which the author describes best practices for working with configuration files in Python. One of the points he makes is that configuration settings should be handled through _identifiers_ rather than strings. This is very good advice, since hacking away at a raw dictionary to extract (key, value) pairs is a risky and error-prone endeavor. Spelling mistakes and type errors come to mind.

## Enter data classes

Fortunately, Python 3.7 introduced [`dataclasses`](https://docs.python.org/3/library/dataclasses.html). Check [this article](https://realpython.com/python-data-classes) for an in-depth guide. In a nutshell, a data class is a class that essentially holds data (although it can have methods as well), and it comes with mandatory type hints. Data classes are kinda like `struct`s in C++.

Here is how we could encapsulate a simple server configuration using a data class:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 </pre></td><td><pre><span>from</span> <span>dataclasses</span> <span>import</span> <span>dataclass</span>  <span>@</span><span>dataclass</span> <span>class</span> <span>ServerConfig</span><span>:</span>     <span>host</span><span>:</span> <span>str</span>     <span>port</span><span>:</span> <span>int</span>     <span>timeout</span><span>:</span> <span>float</span> </pre></td></tr></tbody></table>`

This data class may be instantiated and used as follows:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 </pre></td><td><pre><span>In</span> <span>[</span><span>246</span><span>]:</span> <span>config</span> <span>=</span> <span>ServerConfig</span><span>(</span><span>'example.com'</span><span>,</span> <span>80</span><span>,</span> <span>0.5</span><span>)</span>  <span>In</span> <span>[</span><span>247</span><span>]:</span> <span>config</span> <span>Out</span><span>[</span><span>247</span><span>]:</span> <span>ServerConfig</span><span>(</span><span>host</span><span>=</span><span>'example.com'</span><span>,</span> <span>port</span><span>=</span><span>80</span><span>,</span> <span>timeout</span><span>=</span><span>0.5</span><span>)</span>  <span>In</span> <span>[</span><span>248</span><span>]:</span> <span>config</span><span>.</span><span>host</span> <span>Out</span><span>[</span><span>248</span><span>]:</span> <span>'example.com'</span> </pre></td></tr></tbody></table>`

Data classes are fortunately not limited to attributes. They can have methods, and all the built-in methods including `__init__()` are present. Additionally, there’s `__post_init__()` which is used to post-process the instance after `__init__()` is done.

The data class in the previous example can be modified to accept configuration from a dictionary:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 </pre></td><td><pre><span>@</span><span>dataclass</span> <span>class</span> <span>ServerConfigFromDict</span><span>:</span>     <span>host</span><span>:</span> <span>str</span>     <span>port</span><span>:</span> <span>int</span>     <span>timeout</span><span>:</span> <span>float</span>      <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>conf</span><span>:</span> <span>dict</span><span>):</span>         <span>self</span><span>.</span><span>host</span> <span>=</span> <span>conf</span><span>[</span><span>'host'</span><span>]</span>         <span>self</span><span>.</span><span>port</span> <span>=</span> <span>conf</span><span>[</span><span>'port'</span><span>]</span>         <span>self</span><span>.</span><span>timeout</span> <span>=</span> <span>conf</span><span>[</span><span>'timeout'</span><span>]</span> </pre></td></tr></tbody></table>`

If we try to access a non-existing key from the `conf` dict, a `KeyError` is raised. Notice in this example that we do not check whether the value for `'port'` is an int, nor whether the value for `'timeout'` is a float.

This data class may be instantiated as follows:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 </pre></td><td><pre><span>In</span> <span>[</span><span>263</span><span>]:</span> <span>config</span> <span>=</span> <span>ServerConfigFromDict</span><span>({</span><span>'host'</span><span>:</span> <span>'example.com'</span><span>,</span> <span>'port'</span><span>:</span> <span>80</span><span>,</span> <span>'timeout'</span><span>:</span> <span>0.5</span><span>})</span>  <span>In</span> <span>[</span><span>264</span><span>]:</span> <span>config</span> <span>Out</span><span>[</span><span>264</span><span>]:</span> <span>ServerConfigFromDict</span><span>(</span><span>host</span><span>=</span><span>'example.com'</span><span>,</span> <span>port</span><span>=</span><span>80</span><span>,</span> <span>timeout</span><span>=</span><span>0.5</span><span>)</span>  <span>In</span> <span>[</span><span>265</span><span>]:</span> <span>config</span><span>.</span><span>host</span> <span>Out</span><span>[</span><span>265</span><span>]:</span> <span>'example.com'</span> </pre></td></tr></tbody></table>`

Another solution is to use the [`dacite`](https://pypi.org/project/dacite/0.0.13/) package:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 </pre></td><td><pre><span>In</span> <span>[</span><span>344</span><span>]:</span> <span>data</span> <span>=</span> <span>{</span><span>'host'</span><span>:</span> <span>'example.com'</span><span>,</span> <span>'port'</span><span>:</span> <span>80</span><span>,</span> <span>'timeout'</span><span>:</span> <span>0.5</span><span>}</span>  <span>In</span> <span>[</span><span>345</span><span>]:</span> <span>config</span> <span>=</span> <span>dacite</span><span>.</span><span>from_dict</span><span>(</span><span>data_class</span><span>=</span><span>ServerConfig</span><span>,</span> <span>data</span><span>=</span><span>data</span><span>)</span>  <span>In</span> <span>[</span><span>346</span><span>]:</span> <span>config</span> <span>Out</span><span>[</span><span>346</span><span>]:</span> <span>ServerConfig</span><span>(</span><span>host</span><span>=</span><span>'example.com'</span><span>,</span> <span>port</span><span>=</span><span>80</span><span>,</span> <span>timeout</span><span>=</span><span>0.5</span><span>)</span>  <span>In</span> <span>[</span><span>347</span><span>]:</span> <span>config</span><span>.</span><span>host</span> <span>Out</span><span>[</span><span>347</span><span>]:</span> <span>'example.com'</span> </pre></td></tr></tbody></table>`

## Dynamically creating a configuration class

The previous examples have shown how to transform a dict-based configuration into a data class. However, we had to make assumptions regarding the configuration itself (what keys it actually contains). There may be situations where you just want to load the whole dict without knowing what keys it contains.

We can do this using the Python [`setattr`](https://docs.python.org/3/library/functions.html#setattr) built-in method. We don’t even need a data class for this, a “dumb” class can cut it just as well:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 </pre></td><td><pre><span>class</span> <span>DynamicConfig</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>conf</span><span>):</span>         <span>if</span> <span>not</span> <span>isinstance</span><span>(</span><span>conf</span><span>,</span> <span>dict</span><span>):</span>             <span>raise</span> <span>TypeError</span><span>(</span><span>f</span><span>'dict expected, found </span><span>{</span><span>type</span><span>(</span><span>conf</span><span>).</span><span>__name__</span><span>}</span><span>'</span><span>)</span>          <span>self</span><span>.</span><span>_raw</span> <span>=</span> <span>conf</span>         <span>for</span> <span>key</span><span>,</span> <span>value</span> <span>in</span> <span>self</span><span>.</span><span>_raw</span><span>.</span><span>items</span><span>():</span>             <span>setattr</span><span>(</span><span>self</span><span>,</span> <span>key</span><span>,</span> <span>value</span><span>)</span>  <span>config</span> <span>=</span> <span>DynamicConfig</span><span>({</span><span>'host'</span><span>:</span> <span>'example.com'</span><span>,</span> <span>'port'</span><span>:</span> <span>80</span><span>,</span> <span>'timeout'</span><span>:</span> <span>0.5</span><span>})</span> <span>print</span><span>(</span><span>f</span><span>'host: </span><span>{</span><span>config</span><span>.</span><span>host</span><span>}</span><span>, port: </span><span>{</span><span>config</span><span>.</span><span>port</span><span>}</span><span>, timeout: </span><span>{</span><span>config</span><span>.</span><span>timeout</span><span>}</span><span>'</span><span>)</span> </pre></td></tr></tbody></table>`

Output:

`<table><tbody><tr><td><pre>1 </pre></td><td><pre>host: example.com, port: 80, timeout: 0.5 </pre></td></tr></tbody></table>`

## Dynamic configuration with INI files

The dynamic configuration class we’ve seen above works well for dicts. However, when parsing certain configuration file formats, the output might be something _dict-like_, i.e. close to but not quite a dict.

Take the INI format for instance. Suppose we have a `config.ini` file with the following contents:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 </pre></td><td><pre><span>[server]</span> <span>host</span> <span>=</span> <span>example.com</span> <span>port</span> <span>=</span> <span>80</span> <span>timeout</span> <span>=</span> <span>0.5</span>  <span>[user]</span> <span>username</span> <span>=</span> <span>admin</span> <span>level</span> <span>=</span> <span>10</span> </pre></td></tr></tbody></table>`

INI files may be parsed with [`configparser`](https://docs.python.org/3/library/configparser.html), but the object we get is a `configparser.ConfigParser`. We can create a class to encapsulate such an object and provide identifiers for keys. For the `key = value` part of the INI file, we can reuse our previous `DynamicConfig` class above, but we need to handle the `[sections]` in the INI file separately.

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 </pre></td><td><pre><span>class</span> <span>DynamicConfigIni</span><span>:</span>     <span>def</span> <span>__init__</span><span>(</span><span>self</span><span>,</span> <span>conf</span><span>):</span>         <span>if</span> <span>not</span> <span>isinstance</span><span>(</span><span>conf</span><span>,</span> <span>configparser</span><span>.</span><span>ConfigParser</span><span>):</span>             <span>raise</span> <span>TypeError</span><span>(</span><span>f</span><span>'ConfigParser expected, found </span><span>{</span><span>type</span><span>(</span><span>conf</span><span>).</span><span>__name__</span><span>}</span><span>'</span><span>)</span>          <span>self</span><span>.</span><span>_raw</span> <span>=</span> <span>conf</span>         <span>for</span> <span>key</span><span>,</span> <span>value</span> <span>in</span> <span>self</span><span>.</span><span>_raw</span><span>.</span><span>items</span><span>():</span>             <span>setattr</span><span>(</span><span>self</span><span>,</span> <span>key</span><span>,</span> <span>DynamicConfig</span><span>(</span><span>dict</span><span>(</span><span>value</span><span>.</span><span>items</span><span>())))</span> </pre></td></tr></tbody></table>`

Here is `DynamicConfigIni` in action:

`<table><tbody><tr><td><pre>1 2 3 4 5 </pre></td><td><pre><span>parser</span> <span>=</span> <span>configparser</span><span>.</span><span>ConfigParser</span><span>()</span> <span>parser</span><span>.</span><span>read_file</span><span>(</span><span>open</span><span>(</span><span>'config.ini'</span><span>))</span> <span>config</span> <span>=</span> <span>DynamicConfigIni</span><span>(</span><span>parser</span><span>)</span> <span>print</span><span>(</span><span>'server:'</span><span>,</span> <span>config</span><span>.</span><span>server</span><span>.</span><span>host</span><span>,</span> <span>config</span><span>.</span><span>server</span><span>.</span><span>port</span><span>,</span> <span>config</span><span>.</span><span>server</span><span>.</span><span>timeout</span><span>)</span> <span>print</span><span>(</span><span>'user:'</span><span>,</span> <span>config</span><span>.</span><span>user</span><span>.</span><span>username</span><span>,</span> <span>config</span><span>.</span><span>user</span><span>.</span><span>level</span><span>)</span> </pre></td></tr></tbody></table>`

Output:

`<table><tbody><tr><td><pre>1 2 </pre></td><td><pre>server: example.com 80 0.5 user: admin 10 </pre></td></tr></tbody></table>`

## Conclusion

In this post we’ve seen how to encapsulate configuration settings in Python such that we get identifiers instead of strings for the configuration keys. For a simple usage where we know in advance what keys the configuration contains, we can use data classes. For more advanced use cases it is also possible to use `setattr()` to “objectify” the configuration keys. We have looked at a case study for the INI file format, that may be parsed with `configparser`.

Check out [this article](https://alexandra-zaharia.github.io/posts/use-cases-for-python-environment-variables/) for a discussion of passing configuration options in Python through environment variables.
