'''
 WAP to print Alphabets in reversing order
 Z to A
'''
n = ord('Z')
for i in range(ord('Z'),ord('A')-1,-1):
    print(chr(i), end=" ")