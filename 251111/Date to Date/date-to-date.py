m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

before = 0
for m in range(m1):
    before += days[m]
before += d1

after = 0
for m in range(m2):
    after += days[m]
after += d2

print(after - before)