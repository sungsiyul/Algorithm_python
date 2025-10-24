N = int(input())

# Please write your code here.
def recursive_flower(N):
    if N == 0:
        return
    print(N, end=" ")
    recursive_flower(N-1)
    print(N, end=" ")

recursive_flower(N)