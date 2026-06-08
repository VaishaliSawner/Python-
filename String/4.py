# length of last word 

 
def lengthoflastword(s):
    i=len(s)-1
    counter=0

    while s[i]== " ":
        i-=1
    
    while s[i]!=" ":
        counter +=1
        i -=1
        return counter;

result = 












'''
s = input("Enter string: ")

length = 0
i = len(s) - 1


while i >= 0 and s[i] == ' ':
    i -= 1

while i >= 0 and s[i] != ' ':
    length += 1
    i -= 1

print("Length of last word:", length)
'''

