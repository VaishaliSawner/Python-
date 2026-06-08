# By using Function 
# By using extended class 

from threading import Thread

class FirstThread(Thread):
    def run(self):
        print("Run executed ")



t1=FirstThread()
t2=FirstThread()


t1.start() # -> start() -> run()
t2.start()

