# Check Subset

# number of test cases
t = int(input())

for i in range(t):
    # print(i)
    a = int(input())
    a_set = set(input().split(' '))

    b = int(input())
    b_set = set(input().split(' '))

    if a_set.issubset(b_set):
        print('True')
    else:
        print('False')

