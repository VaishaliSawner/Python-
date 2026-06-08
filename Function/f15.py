x = 500
def outer():
    x = 100 # x : 100 -> outer
    def inner():
        nonlocal x
        x = 200 
        print(f"Inside inner x : {x}")
    
    inner()
    print(f"Inside outer x : {x}")
    


outer()