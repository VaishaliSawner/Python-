# Check  String is Palindrome or not  


# With Function 
s = input("Enter a string")

def isPalindrome(s):
    left=0
    right=len(s)-1

    while left < right:
        if s[left]!= s[right]:
            return False
        left +=1
        right -=1
    else:
         return True
        
print(f"{'Palindrome' if isPalindrome(s) else 'Not Palindrome'}")
    
# WITHOUT Function 
# '''
# s = input("Enter a string: ")

# left = 0
# right = len(s) - 1

# isPalindrome = True

# while left < right:
#     if s[left] != s[right]:
#         isPalindrome = False
#         break
#     left += 1
#     right -= 1

# if isPalindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

    

# # Simple Program Palindrome 

# String = input("Enter the String")
# rev = ""

# for char in String:
#     rev = char +rev
# if String == rev:
#     print("String is palindrome ")
# else:
#     print("String is not palindrome")
# '''



