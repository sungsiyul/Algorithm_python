a, b, c = map(int, input().split())

# Please write your code here.
def get_minutes(a, b, c):
    return a * 24 * 60 + b * 60 + c

print(get_minutes(a, b, c) - get_minutes(11, 11, 11))