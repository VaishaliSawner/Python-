from threading import Thread
import time 


class FirstThread(Thread):
    def run(self):
        for i in range(5):
           print("GM......")
        time.sleep(1.5)

class SecondThread(Thread):
    def run(self):
        for i in range(5):
            print("GN......")
        time.sleep(1.3)

t1=FirstThread()
t2=SecondThread()

t1.start()
t2.start()