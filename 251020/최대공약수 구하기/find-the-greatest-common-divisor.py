n, m = map(int, input().split())

# Please write your code here.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(n, m))