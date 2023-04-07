sugar = int(input())

#5의 배수가 될 때까지 3을 빼주면서 계산
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break
    sugar -= 3
    bag += 1
#break를 통해 탈출했을 때만 print하고 싶다면?
else:
    print(-1)ㅇ