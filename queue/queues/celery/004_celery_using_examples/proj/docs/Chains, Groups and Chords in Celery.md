---
source: https://sayari3.com/articles/18-chains-groups-and-chords-in-celery/ \
created: 2022-12-16T14:30:14 (UTC +01:00) \
tags: [] \
author: 
---
# Chains, Groups and Chords in Celery
---
If you have used Celery with Django before then this tutorial will help you understand a few important concepts. If Celery is new to you , I suggest you check out their [official documentation](https://docs.celeryproject.org/en/stable/#) first just to get familiar with it.

## CHAINS

We are going to use this example task in our examples

```
@app.task
def add(x, y):
    return x + y
```

When we chain tasks together, the second task will take the results of the first task as its first argument, for example

```


from celery import chain

res = chain(add.s(1, 2), add.s(3)).apply_async() 

```

In the above example, you can notice the second task has only one argument , this is because the return value of the first task which in our example is 3 will be the first argument of the second task , the second task will now look like this

```
add.s(3, 3)
```

Hope this image below helps you understand it better

![chains](https://sayari3.com/media/relatedimages/IMG_20210206_103220_291.JPG)

Notice the first argument of _second_ task is 3 and the first argument of _third_ task is 6 which is the result of the _second_ task.

Another way of chaining tasks is using this syntax with pipe symbol ( " | " ).

```
res2 = (add.s(1, 2) | add.s(3)).apply_async()
```

The above code is just the same as this code below, you can choose which one you prefer.

```
 res2 = chain(add.s(1, 2), add.s(3)).apply_async()
```

## GROUPS

Celery documentation says:

> Groups are used to execute tasks in parallel. The group function takes in a list of signatures.

Example code :

```


>>> from celery import group
>>> from tasks import add

>>> job = group([
...             add.s(2, 2),
...             add.s(4, 4),
... ])

>>> result = job.apply_async()

>>> result.ready()  # have all subtasks completed?
True
>>> result.successful() # were all subtasks successful?
True
>>> result.get()
[4, 8 ]


```

Example image to illustrate how groups work

![groups](https://sayari3.com/media/relatedimages/IMG_20210206_185041_088.JPG)

## CHORDS

A Chord usually has two parts, _header_ and _callback_

The syntax looks like this :

```
 
chord(header)(callback)
 
```

The _header_ here is simply a group of tasks, the _callback_ is run or executed after the groups of tasks have finished.

For us to demonstrate how chord works we will need a function which will act as our _callback_.

We will call our callback function **tsum**, it takes in a list of numbers and adds them up.

**tsum:**

```
@app.task
def tsum(numbers):
    return sum(numbers)
```

Chord example:

```
 
>>> callback = tsum.s()
>>> header = [ add.s(2, 2),  add.s(4, 4) ]
>>> result = chord(header)(callback)
>>> result.get()
12

```

The above code is similar to this mathematical expression:

**∑ ((2 + 2) + (4 + 4))**

Image below illustrates how chords work

![chords](https://sayari3.com/media/relatedimages/IMG_20210206_202728_351.JPG)

**Note:**

[Celery documentation](https://docs.celeryproject.org/en/stable/userguide/canvas.html) says we should avoid using chords as much as possible, but you can still use it if you really have to, read more on why you should not use chords on the Celery documentation.

## RESOURCES
