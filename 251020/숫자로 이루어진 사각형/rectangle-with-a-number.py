N = int(input())

# Please write your code here.
def f(N):
    print_number = 1
    for _ in range(N):
        for _ in range(N):
            if print_number == 10:
                print_number = 1
            print(print_number, end = ' ')
            print_number += 1
        print('\n', end = '')

f(N)