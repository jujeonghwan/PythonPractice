# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# thisset.update({"orange", "mango", "grapes"})
# print(thisset)
# print(len(thisset))
# thisset.remove("banana")
# thisset.discard("banana")
# x = thisset.pop()
# print(x)
# thisset.clear()
# del thisset
# print(thisset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# set1.update(set2)
# print(set1)

# thisset = set(("apple", "banana", "cherry"))    # note the double round-brackets
# print(thisset)

# H = set("Hacker")
# R = set("Rank")
# H.update(R)
# H.intersection_update(R)
# H.difference_update(R)
# H.symmetric_difference_update(R)
# print(H)

# the number of elements in set A
A = int(input())

# the space separated list of elements in set A
A_set = set(map(int, input().split()))
# print(A_set)

# the number of other sets.
N = int(input())

for i in range(N):
    # function name & the number of elements in other sets
    input_list = input().split(' ')

    function_name = input_list[0]
    O = int(input_list[1])

    # the space separated list of elements in ohter set
    O_set = set(map(int, input().split()))

    # print(O_set)

    # execute
    # eval('A_set.' + function_name + '(' + O_set + ')')
    # eval('A_set.' + function_name + '(' + set(O_set) + ')')
    getattr(A_set, function_name)(O_set)

print(str(sum(A_set)))

