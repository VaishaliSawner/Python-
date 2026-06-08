'''
  153 :=
  1^3 + 5^3 + 3^3 = 153
'''

n = int(input("Enter a number : "))
digit_length = 0
copy_of_n = n
# calculate the length of number. Finding how many digit in number
while n > 0:
    n = n // 10
    digit_length += 1

# Checking for armstrong..
if digit_length:
 power = digit_length
 n = copy_of_n
 sum = 0
 # n = 153
 while n > 0:
   digit = n % 10
   sum = sum + digit**power
   n = n // 10
 if sum == copy_of_n:
   print("Armstrong...")
 else:
   print("Not Armstrong..")    