n1 = int(input())
l1 = list(map(int, input().split()))

n2 = int(input())
l2 = list(map(int, input().split()))

l1.extend(l2)
l1.sort()

n = len(l1)

if n % 2 == 1:
    print(l1[n // 2])
else:
    print((l1[n // 2 - 1] + l1[n // 2]) / 2)
