import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = [str(x) for x in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    num = num[:i] + num[k:j+1] + num[i:k] + num[j+1:]

for i in range(1, n+1):
    print(num[i], end=" ")
