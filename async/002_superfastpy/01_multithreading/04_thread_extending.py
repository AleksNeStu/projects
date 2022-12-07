# Example of Extending the Thread Class
# Running the example first creates an instance of the thread, then executes the content of the run() function.
from time import sleep
import threading as th

# custom thread class
class CustomThread(th.Thread):
    # override the run function
    # override the run() instance method and define the code that we wish to execute in another thread.
    def run(self):
        # block for a moment
        sleep(2)
        # display a message
        print('From another thread')

# create the thread
thread = CustomThread()
# start the thread
# The code will then run in a new thread as soon as the operating system can schedule it.
# create an instance of our CustomThread class and call the start() function to begin executing our run() function in another thread. Internally, the start() function will call the run() function.
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
print('Main thread done')
