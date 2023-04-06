N = input()
Pi = list(map(int, input().split()))

Pi.sort()

a = 0
time = []
for p in Pi:
    a += p
    time.append(a)

print(sum(time))