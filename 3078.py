"""
이름 길이 마다 큐 생성
등수가 k 이상 차이나면 popleft
이름은 2~20
"""
import sys
from collections import deque

input = sys.stdin.readline

que = [deque([]) for _ in range(21)]

n, k = map(int, input().rsplit())
cnt = 0
for i in range(n):
    name = input().strip()
    name_len = len(name)

    while que[name_len]:
        if i - que[name_len][0][0] <= k:
            cnt += len(que[name_len])
            que[name_len].append([i, name])
            break
        else:
            que[name_len].popleft()

    if not que[name_len]:
        que[name_len].append([i, name])

print(cnt)

