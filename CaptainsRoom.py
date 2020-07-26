# k = int(input())
# L = str(input()).split(" ")
# family = L
# total = set(L)
# for r in set(L):
#     try:
#         family.remove(r)
#     except:
#         pass
# print ("".join((total - set(family))))

# the size of each group.
k = int(input())

# the unordered elements of the room number list
room_numbers = input().split(' ')
# print(room_numbers)

answer = 0

for room_number in room_numbers:
    if (room_numbers.count(room_number) == 1):
        answer = room_number
        break

print(answer)