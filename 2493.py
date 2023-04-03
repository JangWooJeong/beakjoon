import sys

n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, tops[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))


for i in range(1, n+1):
    while stack:
        if tops[-i] > stack[-1][1]:
            answer.append(tops.index(stack[-1][0]))
        else:
            stack.pop()

    stack.append([n-i, tops[-i]])

