from sys import stdin

input = stdin.readline

n = int(input().strip())

ropes = []
temp = [0] * n

for i in range(n):
    ropes.append(int(input().strip()))

ropes = sorted(ropes, reverse=True)

for i in range(len(ropes)):
    temp[i] = ropes[i] * (i + 1)

print(max(temp))