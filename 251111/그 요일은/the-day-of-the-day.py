m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
def get_days(m, d):
    day = 0
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(m-1):
        day += days[i]
    return day + d

before = get_days(m1, d1)
after = get_days(m2, d2)

between_days = after - before

between_weeks = between_days // 7
rest_days = between_days % 7

day_of_week = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

if rest_days >= day_of_week[A]:
    between_weeks += 1

print(between_weeks)