N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for _ in range(N):
    result += max(A) * min(B)
    A.pop(A.index(max(A)))
    B.pop(B.index(min(B)))

print(result)