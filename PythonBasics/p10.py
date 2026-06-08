'''
  Bitwise operator :-
  &
  |
  ^
  <<
  >>
  n >> 3
  if n is even then n/2
  if n is odd then (n-1)/2
  ~

  c/c++/java
  int :-  4 byte 32-bit
   3 << 2

  2**2 * 3
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(f"Before swapping a : {a} and b : {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swapping a : {a} and b : {b}")