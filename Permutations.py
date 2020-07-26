from itertools import permutations

# print(permutations(['1', '2', '3']))

# print(list(permutations(['1', '2', '3'])))

# print(list(permutations(['1', '2', '3'], 2)))

# print(list(permutations('abc', 3)))

S, k = list(input().split())
# print(S)
# print(k)

# print(list(permutations(S, int(k))))
perList = list(permutations(S, int(k)))
perList.sort()

for i in perList:
    print("".join(i))


