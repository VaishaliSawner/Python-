# Leetcode 1221 
 

def balanced(s):
    icount=0
    rcount=0
    counter=0


    for ch in s:
        if ch == "R":
            rcount+=1
        else:
            icount+=1
        

        if rcount == icount:
            counter +=1
        
    return counter
    
s="RLRRLLRLRL"

print(f"Possible substrings : {balanced(s)}")