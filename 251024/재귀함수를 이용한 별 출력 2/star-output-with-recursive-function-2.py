n = int(input())

# Please write your code here.
def print_stars(n):
    if n == 0: return
    print('* ' * n)
    print_stars(n-1)
    print('* ' * n)

print_stars(n)