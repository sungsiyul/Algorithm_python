equation = input().split('-')

result = 0
for i, equ in enumerate(equation):
    eq = equ.split('+')
    for e in eq:
        if i == 0:
            result += int(e)
        else:
            result -= int(e)
print(result)