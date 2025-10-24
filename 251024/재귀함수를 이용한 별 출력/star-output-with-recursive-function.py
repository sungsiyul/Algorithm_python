n = int(input())

# Please write your code here.
def print_star_tree(N):
    if N == 0:
        return
    print_star_tree(N-1)
    print("*" * N)

print_star_tree(n)