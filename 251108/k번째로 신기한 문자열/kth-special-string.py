n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
cnt = 0
sorted_str = sorted(str)
for s in sorted_str:
    if s[:len(t)] == t:
        cnt += 1
        if cnt == k:
            print(s)
            break