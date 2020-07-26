from itertools import product

# print (list(product([1, 2, 3], repeat = 2)))

# print (list(product([1, 2, 3], [3, 4])))

# A = [[1, 2, 3], [3, 4, 5]]
# print(list(product(*A)))

# B = [[1, 2, 3], [3, 4, 5], [7, 8]]
# print(list(product(*B)))

# A_list = list(map(int, input().split(' ')))

A_list = list(map(int, input().split(' ')))
B_list = list(map(int, input().split(' ')))

# print(list(product(A_list, B_list)))
print(*product(A_list, B_list))