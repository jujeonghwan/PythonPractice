
n, m = input().split()

n_array = input().split()
A_array = input().split()
B_array = input().split()

print (sum([(i in A_array) - (i in B_array) for i in n_array]))

"""
happiness = 0

for i in n_array:
    if i in A_array:
        happiness += 1
    if i in B_array:
        happiness -= 1

print (happiness)
"""



