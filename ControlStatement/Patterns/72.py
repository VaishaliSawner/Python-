
'''
a
ab
abc
abcd
abcde

'''




for i in range(1,6):
    for j in range(1,i+1):
        print(chr(96+j),end="")
    print()