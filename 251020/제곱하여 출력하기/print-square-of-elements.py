N = int(input())


N_list = list(map(int, input().split()))


for i in range(N):
    print(N_list[i]**2, end=' ')