# Example of Extending the Thread Class and Returning Values
# We may need to retrieve data from the thread, such as a return value.
# There is no way for the run() function to return a value to the start() function and back to the caller.
# Instead, we can return values from our run() function by storing them as instance variables and having the caller retrieve the data from those instance variables.
#  indirectly return a value from the extended threading.Thread class.
import threading as th
from time import sleep


#  update the run() function to store some data as an instance variable (also called a Python attribute).
# custom thread class
class CustomThread(th.Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(2)
        # display a message
        print('From another thread')
        # store return value
        self.value = 99

# Next, we can retrieve the “returned” (stored) value from the run function in the main thread.
# get the value returned from run
# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
# get the value returned from run
value = thread.value
print(f'Got: {value}')