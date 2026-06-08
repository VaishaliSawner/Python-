def f1(a): # a = (1,2,3) :-- 3000
  print(f"Before concat : a {id(a)}")
  a = a + (5,6) # (1,2,3,5,6) :--- 5000
  print(f"Inside f1 : {a} address of a {id(a)}")
  pass


x = (1,2,3)
print(f"Address of x {id(x)}")
print(f"Before calling f1 : {x}")
f1(x)
print(f"After calling f1 {x}")    