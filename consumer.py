import threading
import queue
import string
import random
from pwdCheckThread import PwdCheckThread

class PasswordConsumer(threading.Thread):
    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        password = None
        while True:
            self.condition.acquire()
            try:

                password = self.queue.get(block=False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            if not password is None:
                #print("Testing with 123: "+str(password.check("123")))string.ascii_uppercase +
                testLen = 3
                #tryis = 0
                #while True:
                  #  lenf=random.randint(1, testLen)
                 #   randPwd = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for i in range(lenf))
                 #   print("Checking PWD: "+randPwd)
                 #   tryis=tryis+1
                  #  if password.check(randPwd):
                 #       print("Password found after "+str(tryis)+" attemps! Password is "+randPwd)
                 #       break
                checkThread1 = PwdCheckThread(testlen=testLen, password=password)

                checkThread1.setDaemon(True)

                checkThread1.start()
                checkThread1.join()

                checkThread2 = PwdCheckThread(testlen=testLen, password=password)

                checkThread2.setDaemon(True)

                checkThread2.start()
                checkThread2.join()

                checkThread3 = PwdCheckThread(testlen=testLen, password=password)

                checkThread3.setDaemon(True)

                checkThread3.start()
                checkThread3.join()