n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
import heapq as hq

heap = []
for num in nums:
    hq.heappush(heap, num)

for _ in range(k-1):
    hq.heappop(heap)

print(heap[0])