s = input("Enter string: ").lower()

vowels = "aeiou"
v_count = {}
c_count = {}

for ch in s:
    if ch >= 'a' and ch <= 'z':
        if ch in vowels:
            if ch in v_count:
                v_count[ch] += 1
            else:
                v_count[ch] = 1
        else:
            if ch in c_count:
                c_count[ch] += 1
            else:
                c_count[ch] = 1























'''                

# Find max vowel
max_vowel = ''
max_v = 0

for k in v_count:
    if v_count[k] > max_v:
        max_v = v_count[k]
        max_vowel = k

# Find max consonant
max_cons = ''
max_c = 0

for k in c_count:
    if c_count[k] > max_c:
        max_c = c_count[k]
        max_cons = k

print("Most frequent vowel:", max_vowel)
print("Most frequent consonant:", max_cons)


'''