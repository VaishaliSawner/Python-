from threading import Thread

class FirstThread(Thread):
    def run(self):
        for i in range(5):
            print("GM......")



class SecondThread(Thread):
    def run(self):
        for i in range(5):
            print("GN......")


t1=FirstThread()  # New/Born State 
t1.start()  #Runable
t2=SecondThread()
t2.start()    #Runnable