
# remove(x)
"""
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(5)
print (s)


print (s.remove(4))
print (s)

s.remove(0)
"""

# discard(x)
"""
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.discard(5)
print(s)

print (s.discard(4))

print (s)

s.discard(0)
print (s)
"""

# pop()
"""
s = set([1])
print (s.pop())

print (s)

print (s.pop())
"""


n = int(input())
s = set(map(int, input().split()))
# print(s)

for i in range(int(input())):   # if 10, then 0, 1, ... 9
    input_list = input().split(' ')

    if (len(input_list) > 1):
        eval('s.' + input_list[0] + '(' + input_list[1] + ')')
    else:
        eval('s.' + input_list[0] + '()')
        
print(sum(s))

