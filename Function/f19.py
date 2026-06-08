# map(), filter(), reduce()
# Decorator
def f1(func):
    print("F1 executedd....")
    func()

def wish():
    print("Good morning..")

f1(wish)    