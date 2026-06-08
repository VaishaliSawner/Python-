def outer():
    x = 100
    def inner():
        print(f"Inside inner x : {x}")
    print(f"Outer function executed...x : {x}")
    return inner

inner = outer()
print("Hello....")
print("Hi.......")
inner()    