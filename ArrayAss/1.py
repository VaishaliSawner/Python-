
'''
arr = [1, 2, 3]
n = len(arr)

for i in range(n):
    if (i == 0 or arr[i] >= arr[i-1]) and (i == n-1 or arr[i] >= arr[i+1]):
        print("Peak element index:", i)
        break

'''

lst =[1,5,4,2,6,7]
print(lst)
n=len(lst)
if n==1:
    print() 