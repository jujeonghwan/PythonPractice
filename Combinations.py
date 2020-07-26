from itertools import combinations

# Jeonghwan
# print(list(combinations('12345', 2)))

# A = [1,1,3,3,3]
# print(type(A))
# print(list(combinations(A,4)))

A, k = list(input().split())
# print(type(A))

A2 = sorted(A)
A3 = "".join(A2)

for i in range(int(k)):
    combiList = list(combinations(A3, i + 1))

    for x in combiList:
        print("".join(x))

""" Oher
s, n = raw_input().split()

for i in range(1, int(n) + 1):
    for j in combinations(sorted(s), i):
        print ("".join(j))
"""