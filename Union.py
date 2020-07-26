"""
A = {'a', 'c', 'd'}
B = {'c', 'd', 2}
C = {1, 2, 3}


print('A U B = ', A.union(B))
print('B U C = ', B.union(C))
print('A U B U C = ', A.union(B, C))
print('A.union() = ', A.union())


print('A U B =', A | B)
print('B U C = ', B | C)
print('A U B U C = ', A | B | C)


s = set("Hacker")

print(s.union("Rank"))

print(s.union(set(['R', 'a', 'n', 'k'])))

print(s.union(['R', 'a', 'n', 'k']))

print(s.union(enumerate(['R', 'a', 'n', 'k'])))

print(s.union({"Rank":1}))

s | set("Rank")


my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list, 1):
    print(counter, value)


my_list = ['apple', 'banana', 'grapes', 'pear']
# print(type(enumerate(my_list, 1)))
counter_list = list(enumerate(my_list, 1))
print(counter_list)
print(type(counter_list))
"""

n = int(input())
n_set = set(map(int, input().split()))

b = int(input())
b_set = set(map(int, input().split()))

union_set = n_set.union(b_set)
print(len(union_set))