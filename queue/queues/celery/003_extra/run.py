import sys
import os


from proj.tasks import add



res = add.delay(1, 2)
print(res.status)
print(res.result)
print(res.get())


# https://docs.celeryq.dev/en/latest/userguide/calling.html#basics
res = add.apply_async((2, 22), countdown=3)
result = res.get()    # this takes at least 3 seconds to return
print(result)