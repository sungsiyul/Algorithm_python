n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

# 수열 A (길이 N)
# M개의 정수 쌍 a1, a2
# M 번을 걸쳐 a1 ~ a2번째 합 출력

for a1, a2 in queries:
    print(sum(arr[a1-1:a2]))
