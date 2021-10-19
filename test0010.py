for i in range(10):     # == range(0, 10), ==range(0, 10, 1) 0 ~ 9
    # print(i)     # 이 뒤에 \n 이 생략되어 있음
    print(i, end=' ')   # 한 줄로 출력해준다.
print()

for i in range(0, 10, 2):
    print(i, end=' ')
print()

# [문제] 1에서 100이하까지 홀수를 한 줄로 출력하시오.
for i in range(1, 101, 2):
    print(i, end=" ")