a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cal(a, o, c):
    if o == '+':
        return a+c
    elif o == '-':
        return a-c
    elif o == '/':
        return int(a/c)
    elif o == '*':
        return a*c
    else:
        return False

print(def(cal(a, o, c)))