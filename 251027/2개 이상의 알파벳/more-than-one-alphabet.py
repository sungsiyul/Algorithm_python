A = input()

# Please write your code here.
from collections import defaultdict
def f(A):
    temp = defaultdict(int)
    for a in A:
        temp[a] += 1
    if len(temp) == 1:
        return False
    else:
        return True

print("Yes" if f(A) else "No")
