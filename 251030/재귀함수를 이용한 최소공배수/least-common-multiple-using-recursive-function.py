n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

lcm_v = 1
for i in range(len(arr)-1):
    arr[i+1] = lcm(arr[i], arr[i+1])
print(arr[-1])