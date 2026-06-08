# leetcode 771
#jewels= "aA"
#stones = "aAAbbbb"

jewels= "Bb"
stones = "bbBBB"

#jewels = input("Enter jewels: ")
#stones = input("Enter stones: ")


def check():
    count = 0

    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                count += 1

    return count
print(check())

'''
jewels = input()
stones = input()

jewel_set = set(jewels)
count = 0

for stone in stones:
    if stone in jewel_set:
        count += 1

print(count)







'''