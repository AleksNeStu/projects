"""
This module provides APIs to manage, store, and access context-local state. The ContextVar class is used to declare and work with Context Variables. The copy_context() function and the Context class should be used to manage the current context in asynchronous frameworks.

Context managers that have state should use Context Variables instead of threading.local() to prevent their state from bleeding to other code unexpectedly, when used in concurrent code.
"""
from contextvars import ContextVar, Context, copy_context


var: ContextVar[int] = ContextVar('var', default=42)

assert var.get() == 42

token = var.set('new value')
# code that uses 'var'; var.get() returns 'new value'.

assert var.get() == "new value"

# Reset the context variable to the value it had before the ContextVar.set() that created the token was used.
var.reset(token)

assert var.get() == 42

# After the reset call the var has no value again, so
# var.get() would raise a LookupError.