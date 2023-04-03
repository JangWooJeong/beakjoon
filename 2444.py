num = int(input())

for i in range(1, num+1):
    a = " " * (num - i) + "*"*(2*(i-1)+1)
    print(a)

for i in range(num-1, 0, -1):
    a = " " * (num - i) + "*" * (2 * (i - 1) + 1)
    print(a)
