n, m = input().split()

num = [str(x+1) for x in range(int(n))]
num = ''.join(num)

for _ in range(int(m)):
    i, j, k = map(int, input().split())
    num = num[:i] + num[k+1:j+1] + num[i+1:k] + num[j:]
    print(num)

print(num)
