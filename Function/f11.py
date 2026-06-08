'''
  Argument :-
    Mutable
    Immutable
'''
def f1(a,b=0):
    b = b + 1
    print(f"Inside f1 a : {a} and b : {b}")

f1(10)
f1(10)
f1(10)


def f1():
    global x
    x = 100
    print(f"Inside f1 : {x}")

def f2():
    print(f"Inside f2 : {x}")


f1()
f2()        