# 125 Leetcode 
# Palindrome with special character like , _ 1, 

s = input("Enter the string")


def isPalindrome(s):
    left =0 
    right= len(s)-1
    s =s.lower()

    while left < right:
        while left <right and not s[left].isalnum():
            left +=1
        while left <right and not s[right].isalnum():
            right -=1

        if s[left]!=s[right]:
            return False
        left +=1
        right -=1

    else:
        return True
    
print(f"{'Palindrome' if isPalindrome(s) else 'Not Palindrome'}")


