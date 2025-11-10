m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

before = 0
for m in range(m1-1):
    before += days[m]
before += d1

after = 0
for m_ in range(m2-1):
    after += days[m_]
after += d2

print(after - before + 1)