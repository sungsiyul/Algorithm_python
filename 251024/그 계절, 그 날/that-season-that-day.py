Y, M, D = map(int, input().split())

# Please write your code here.
def check_season(M):
    if M >= 3 and M <= 5: return "Spring"
    elif M >= 6 and M <= 8: return "Summer"
    elif M >= 9 and M <= 11: return "Fall"
    elif M == 12 or M <= 2: return "Winter"
    else: return -1

def check_leap(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True
    return False

def check_last_day(Y, M, D):
    if M == 2:
        if check_leap(Y):
            return 29
        else:
            return 28
    elif M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    else:
        return 31
        
if D > check_last_day(Y, M, D):
    print(-1)
else:
    print(check_season(M))
