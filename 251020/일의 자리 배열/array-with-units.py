a, b = map(int, input().split())

result = [a, b]
for _ in range(8):
    result.append((result[-2] + result[-1]) % 10)

for r in result:
    print(r, end=' ')

