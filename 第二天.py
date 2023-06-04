"""tmp = [1, 2, 3, 4, 5, 6]
print(tmp[5::-2])"""

"""
strs = " I like python "
one = strs.strip()

tow = strs.rstrip()
print(one)
print(tow)
"""
"""
info = {"name": "班长"}
age = info.get("age")
print(age)

age = info.get("age", 18)
print(age)
"""




import math
def sieve(size):
    sieve = [True] * size
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        k = i * 2
        while k < size:
            sieve[k] = False
            k += i
    return sum(1 for x in sieve if x)


print(sieve(100))
