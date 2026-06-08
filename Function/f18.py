def DataEncapsulation():
    counter = 100
    def increment():
        nonlocal counter
        counter = counter + 1
        print(f"Inside increment : {counter}")
    def decrement():
        nonlocal counter
        counter = counter - 1
        print(f"Inside decrement : {counter}")

    return increment,decrement  # (increment,decrement)

increment, decrement = DataEncapsulation()

increment() # 101
increment() # 102
increment() # 103
decrement() # 102
decrement() # 101