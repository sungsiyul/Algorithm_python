a, b = map(int, input().split())

# Please write your code here.
def f(a, b):
    result = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            result += 1
        elif '3' in str(i) or '6' in str(i) or '9' in str(i):
            result += 1
    return result

print(f(a, b))