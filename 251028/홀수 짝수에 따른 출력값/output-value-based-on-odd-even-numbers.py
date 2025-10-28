N = int(input())

# Please write your code here.
def even_odd(N):
    if N <= 2:
        return N
    return N + even_odd(N-2)

print(even_odd(N))    