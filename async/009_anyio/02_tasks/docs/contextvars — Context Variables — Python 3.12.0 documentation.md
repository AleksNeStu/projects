---
source: https://docs.python.org/3/library/contextvars.html

created: 2023-10-26T17:39:48 (UTC +02:00)

tags: []

author: 

---
# contextvars — Context Variables — Python 3.12.0 documentation
---
___

This module provides APIs to manage, store, and access context-local state. The [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar") class is used to declare and work with _Context Variables_. The [`copy_context()`](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "contextvars.copy_context") function and the [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context") class should be used to manage the current context in asynchronous frameworks.

Context managers that have state should use Context Variables instead of [`threading.local()`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") to prevent their state from bleeding to other code unexpectedly, when used in concurrent code.

See also [**PEP 567**](https://peps.python.org/pep-0567/) for additional details.

New in version 3.7.

## Context Variables[¶](https://docs.python.org/3/library/contextvars.html#context-variables "Permalink to this headline")

_class_ contextvars.ContextVar(_name_\[, _\*_, _default_\])[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "Permalink to this definition")

This class is used to declare a new Context Variable, e.g.:

```
var: ContextVar[int] = ContextVar('var', default=42)

```

The required _name_ parameter is used for introspection and debug purposes.

The optional keyword-only _default_ parameter is returned by [`ContextVar.get()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.get "contextvars.ContextVar.get") when no value for the variable is found in the current context.

**Important:** Context Variables should be created at the top module level and never in closures. [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context") objects hold strong references to context variables which prevents context variables from being properly garbage collected.

name[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.name "Permalink to this definition")

The name of the variable. This is a read-only property.

New in version 3.7.1.

get(\[_default_\])[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.get "Permalink to this definition")

Return a value for the context variable for the current context.

If there is no value for the variable in the current context, the method will:

-   return the value of the _default_ argument of the method, if provided; or
    
-   return the default value for the context variable, if it was created with one; or
    
-   raise a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError").
    

set(_value_)[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "Permalink to this definition")

Call to set a new value for the context variable in the current context.

The required _value_ argument is the new value for the context variable.

Returns a [`Token`](https://docs.python.org/3/library/contextvars.html#contextvars.Token "contextvars.Token") object that can be used to restore the variable to its previous value via the [`ContextVar.reset()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "contextvars.ContextVar.reset") method.

reset(_token_)[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "Permalink to this definition")

Reset the context variable to the value it had before the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set") that created the _token_ was used.

For example:

```
var = ContextVar('var')

token = var.set('new value')
# code that uses 'var'; var.get() returns 'new value'.
var.reset(token)

# After the reset call the var has no value again, so
# var.get() would raise a LookupError.

```

_class_ contextvars.Token[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token "Permalink to this definition")

_Token_ objects are returned by the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set") method. They can be passed to the [`ContextVar.reset()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "contextvars.ContextVar.reset") method to revert the value of the variable to what it was before the corresponding _set_.

var[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token.var "Permalink to this definition")

A read-only property. Points to the [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar") object that created the token.

old\_value[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token.old_value "Permalink to this definition")

A read-only property. Set to the value the variable had before the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set") method call that created the token. It points to [`Token.MISSING`](https://docs.python.org/3/library/contextvars.html#contextvars.Token.MISSING "contextvars.Token.MISSING") if the variable was not set before the call.

MISSING[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token.MISSING "Permalink to this definition")

A marker object used by [`Token.old_value`](https://docs.python.org/3/library/contextvars.html#contextvars.Token.old_value "contextvars.Token.old_value").

## Manual Context Management[¶](https://docs.python.org/3/library/contextvars.html#manual-context-management "Permalink to this headline")

contextvars.copy\_context()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "Permalink to this definition")

Returns a copy of the current [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context") object.

The following snippet gets a copy of the current context and prints all variables and their values that are set in it:

```
ctx: Context = copy_context()
print(list(ctx.items()))

```

The function has an O(1) complexity, i.e. works equally fast for contexts with a few context variables and for contexts that have a lot of them.

_class_ contextvars.Context[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context "Permalink to this definition")

A mapping of [`ContextVars`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar") to their values.

`Context()` creates an empty context with no values in it. To get a copy of the current context use the [`copy_context()`](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "contextvars.copy_context") function.

Every thread will have a different top-level [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context") object. This means that a [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar") object behaves in a similar fashion to [`threading.local()`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") when values are assigned in different threads.

Context implements the [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") interface.

run(_callable_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.run "Permalink to this definition")

Execute `callable(*args, **kwargs)` code in the context object the _run_ method is called on. Return the result of the execution or propagate an exception if one occurred.

Any changes to any context variables that _callable_ makes will be contained in the context object:

```
var = ContextVar('var')
var.set('spam')

def main():
    # 'var' was set to 'spam' before
    # calling 'copy_context()' and 'ctx.run(main)', so:
    # var.get() == ctx[var] == 'spam'

    var.set('ham')

    # Now, after setting 'var' to 'ham':
    # var.get() == ctx[var] == 'ham'

ctx = copy_context()

# Any changes that the 'main' function makes to 'var'
# will be contained in 'ctx'.
ctx.run(main)

# The 'main()' function was run in the 'ctx' context,
# so changes to 'var' are contained in it:
# ctx[var] == 'ham'

# However, outside of 'ctx', 'var' is still set to 'spam':
# var.get() == 'spam'

```

The method raises a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") when called on the same context object from more than one OS thread, or when called recursively.

copy()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.copy "Permalink to this definition")

Return a shallow copy of the context object.

var in context

Return `True` if the _context_ has a value for _var_ set; return `False` otherwise.

context\[var\]

Return the value of the _var_ [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar") variable. If the variable is not set in the context object, a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised.

get(_var_\[, _default_\])[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.get "Permalink to this definition")

Return the value for _var_ if _var_ has the value in the context object. Return _default_ otherwise. If _default_ is not given, return `None`.

iter(context)

Return an iterator over the variables stored in the context object.

len(proxy)

Return the number of variables set in the context object.

keys()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.keys "Permalink to this definition")

Return a list of all variables in the context object.

values()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.values "Permalink to this definition")

Return a list of all variables’ values in the context object.

items()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.items "Permalink to this definition")

Return a list of 2-tuples containing all variables and their values in the context object.

## asyncio support[¶](https://docs.python.org/3/library/contextvars.html#asyncio-support "Permalink to this headline")

Context variables are natively supported in [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") and are ready to be used without any extra configuration. For example, here is a simple echo server, that uses a context variable to make the address of a remote client available in the Task that handles that client:

```
import asyncio
import contextvars

client_addr_var = contextvars.ContextVar('client_addr')

def render_goodbye():
    # The address of the currently handled client can be accessed
    # without passing it explicitly to this function.

    client_addr = client_addr_var.get()
    return f'Good bye, client @ {client_addr}\n'.encode()

async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info('socket').getpeername()
    client_addr_var.set(addr)

    # In any code that we call is now possible to get
    # client's address by calling 'client_addr_var.get()'.

    while True:
        line = await reader.readline()
        print(line)
        if not line.strip():
            break
        writer.write(line)

    writer.write(render_goodbye())
    writer.close()

async def main():
    srv = await asyncio.start_server(
        handle_request, '127.0.0.1', 8081)

    async with srv:
        await srv.serve_forever()

asyncio.run(main())

# To test it you can use telnet:
#     telnet 127.0.0.1 8081

```
