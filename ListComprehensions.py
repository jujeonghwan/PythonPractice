"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
"""

x = 2
y = 2
z = 2
n = 2

listAnswer = []
idx = -1

for i in range (x + 1):
    for j in range (y + 1):
        for k in range (z + 1):
            if i + j + k != n:
                idx += 1
                listAnswer.append([])
                listAnswer[idx] = [i, j, k]

print (listAnswer)




