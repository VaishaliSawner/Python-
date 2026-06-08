'''
Tuple itself is immutable , but contained objects may be mutable.

'''

t = ([1,2] , [3,4])
t[0].append(100)
print(t)

'''
Output:
([1,2,100], [3,4])
Tuple reference immutable, not internal object

'''



















































'''
Q5 :

Why Tuple Can Contain Mutable Objects?

Ye concept thoda tricky hai 😄
Main ekdum simple way mein samjhata hu.

Pehle Tuple Kya Hota Hai?

Tuple:
✔ immutable hota hai

Matlab:

tuple ko directly change nahi kar sakte.

Example:

t = (1,2,3)

t[0] = 100

Output:

TypeError
Ab Important Twist 😄

Tuple ke ANDAR mutable objects ho sakte hain.

Example:

t = ([1,2], [3,4])

Yaha:

outer object = tuple
inner objects = lists
Tuple Immutable Hai…

BUT Lists Mutable Hain 😄

Ab Ye Dekho
t[0].append(100)

print(t)

Output:

([1,2,100], [3,4])
Confusion 😵

Tum sochoge:

"Tuple immutable tha…
fir change kaise hua?"

Actual Reason 😄

Tuple khud change nahi hua.

Bas:
andar wali list modify hui.

Samjho Carefully

Tuple kya store karta hai?

✔ references

Yani:

t ---> list1
t ---> list2
Immutable Means Kya?

Tuple ke references change nahi ho sakte.

Example:

❌ Not allowed:

t[0] = [100]

Kyuki:

tuple ka item replace kar rahe ho
BUT Allowed 😄
t[0].append(100)

Kyuki:

tuple change nahi hua
list object change hui
Real Life Example 😄

Socho tuple ek locker hai.

Locker fixed hai 🔒
(change nahi ho sakta)

BUT locker ke andar ki books change kar sakte ho 😄

MOST IMPORTANT Interview Line 😄

Tuple is immutable, but it can contain mutable objects.
The tuple references cannot change, but the internal mutable objects can still be modified.

Simple Difference
What Changes?	Allowed?
tuple item replace	❌ No
inner mutable object modify	✔ Yes
Example
Not Allowed ❌
t[0] = [5,6]
Allowed ✔
t[0].append(100)


















'''