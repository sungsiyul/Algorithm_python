N, k = list(map(int, input().split()))

coin_list = [int(input()) for _ in range(N)]

coin_list.sort(reverse=True)

count = 0
for coin in coin_list:
    count = count + k//coin
    k = k % coin

print(count)
