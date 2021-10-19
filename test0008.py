# 제어문 : if문  (노트에 적기)

a = 5

if a >= 3:
    print('3이상')
elif a > 1:     # else if
    print('3미만 1초과')
else:
    print('1이하')

# [문제] 두 숫자를 한 줄에 입력 받아 더 큰 수를 출력하는 프로그램을 만드시오
# [입력] 8 3
# [출력] 8
n1,n2=map(int, input().split())
if n1 > n2:
    print(n1)
else:
    print(n2)



# [문제] 숫자를 하나 입력 받아 70점 이상이면 '최우수'
# 그 외 50점 이상이면 '우수'
# 그 외 20점 이상이면 '보통'
# 그 외는 '노력 필요'를 출력하는 프로그램을 만드시오.
k=int(input())
if k >= 70:
    print("최우수")
elif k >= 50:
    print("우수")
elif k >= 20:
    print("보통")
else:
    print("노력 필요")
