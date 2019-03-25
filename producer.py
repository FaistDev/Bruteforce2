import threading
import queue
from password import Password

class PwdProducer(threading.Thread):

    def __init__(self, queue, condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while(True):

            password = input("Next PWD: \n")

            self.condition.acquire()

            try:
                self.queue.put(Password(password), block=False)
                self.condition.notify()
            except queue.Full:
                self.condition.wait()

            self.condition.release()