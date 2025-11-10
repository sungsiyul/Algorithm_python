m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
def get_days(m, d):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(m-1):
        day += days[i]
    day += d
    return day

def get_day_of_week(day1, day2):
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return day_of_week[(day2 - day1) % 7]
    
print(get_day_of_week(get_days(m1, d1), get_days(m2, d2)))
