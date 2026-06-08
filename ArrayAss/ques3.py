# Sum of even even and odd 

arr = [1,2,3,4,5,6]

even_sum=0
odd_sum=0

for num in arr:
    if num%2==0:
        even_sum=even_sum+num
    else:
        odd_sum=odd_sum+num

print("Even sum = ",even_sum)
print("Odd sum=",odd_sum)