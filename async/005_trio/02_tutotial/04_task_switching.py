"""
We want to watch trio.run() at work, which we can do by writing a class we’ll call Tracer, which implements Trio’s
Instrument interface. Its job is to log various events as they happen:
"""
