import sys

n, k = map(int, sys.stdin.readline().split())
num = [x for x in range(1, n+1)]

answer = []
idx = 0

for i in range(n):
    idx += k - 1
    if idx >= len(num):
        idx = idx % len(num)
    answer.append(str(num.pop(idx)))

print("<", ", ".join(answer), ">", sep='')
