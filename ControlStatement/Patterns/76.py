'''
a
bc
def
ghij
klmno


'''




count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(count+96),end="")
        count+=1
    print()