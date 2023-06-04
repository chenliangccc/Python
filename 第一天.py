import random


# 第一题
"""
strs = "I like python and java"
one = strs.find("n")

print(one)

two = strs.rfind("n")
print(two)
"""

# 第二题
"""
a = [['1']*3 for i in range(3)]
print(a)

b = [['1']]*3
print(b)

c = []
for i in range(3):
    lis = ['1']*3
    c.append(lis)
print(c)

d = []
lis = ['1']*3
for i in range(3):
    d.append(lis)
print(d)
"""

# 第三题

"""
def dec(f):
    n = 3

    def wrapper(*args, **kw):
        return f(*args, **kw) * n
    return wrapper


@dec
def foo(n):
    return n * 2


print(foo(2))
"""

# 第四题
# 对于下面的python3函数，如果输入的参数n非常大，函数的返回值会趋近于以下哪一个值（选项中的值用Python表达式来表示）（）
# (math.pi - 2) / (4 - math.pi)

"""
def foo(n):
    random.seed()
    c1 = 0
    c2 = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        # 以原点为圆心
        r1 = x * x + y * y
        # 以坐标(1,1)为圆心
        r2 = (1 - x) * (1 - x) + (1 - y) * (1 - y)
        if r1 <= 1 and r2 <= 1:
            c1 += 1
        else:
            c2 += 1
    return c1 / c2


print(foo(200000))
"""

# 第五题
"""
sets = {1, 2, 3, 4, 5}
# python中集合set主要利用其唯一性，及并集|、交集&等操作，但不可以直接通过下标进行访问，必须访问时可以将其转换成list再访问
print(sets[2])
"""
# data = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
# print(data)


class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    z = {'i': i, 'j': j}
                    return z


a = Solution()
b = a.twoSum([1, 2, 2, 3, 11, 15, 22], 14)
print(b)
