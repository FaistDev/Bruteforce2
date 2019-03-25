import threading
import random
import string
from password import Password
import queue
import sys

class PwdCheckThread(threading.Thread):

    def __init__(self,testlen,password):
        threading.Thread.__init__(self)
        self.testLen = testlen
        self.password = password

    def run(self):
        tryis=0
        while True:
            lenf = random.randint(1, self.testLen)
            randPwd = ''.join(
                random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(lenf))
            print(str(threading.get_ident())+"Checking PWD: " + randPwd)
            tryis = tryis + 1
            if self.password.check(randPwd):
                print(str(threading.get_ident())+"Password found after " + str(tryis) + " attemps! Password is " + randPwd)
                # Stop all other threads
                sys.exit()
                #