'''
  Calculate the factorial of a number :-
  n = 5
  5 * 4 * 3 * 2 * 1 = 120

  1 * 2 * 3 * 4 * 5 = 120
'''

n = int(input("Enter a numnber : "))
f = 1

for i in range(2,n+1):
    f = f * i
else:
 print("Factorial of {} is {}".format(n,f))