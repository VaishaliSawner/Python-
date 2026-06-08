# Length of last Word in given String

s = input("Enter a string: ")
length = 0
for i in range(len(s)-1 ,-1,-1):
  if s[i] == ' ':
    if length > 0: 
      break
  else:
      length +=1
print(length)

      