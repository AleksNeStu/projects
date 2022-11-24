import sys, time, threading, abc
from optparse import OptionParser

def parse_options():
    parser = OptionParser()
    parser.add_option("-t", action="store", type="int", dest="threadNum", default=1,
                      help="thread count [1]")
    (options, args) = parser.parse_args()
    return options

class thread_sample(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.kill_received = False

    def run(self):

        while not self.kill_received:
            # your code
            print(self.name, "is active")
            time.sleep(1)

def has_live_threads(threads):
    return True in [t.is_alive() for t in threads]

def main():
    options = parse_options()
    threads = []

    for i in range(options.threadNum):
        thread = thread_sample("thread#" + str(i))
        thread.start()
        threads.append(thread)

    while has_live_threads(threads):
        try:
            # synchronization timeout of threads kill
            [t.join(1) for t in threads
             if t is not None and t.is_alive()]
        except KeyboardInterrupt:
            # Ctrl-C handling and send kill to threads
            print("Sending kill to threads...")
            for t in threads:
                t.kill_received = True

    print("Exited")

if __name__ == '__main__':
    main()