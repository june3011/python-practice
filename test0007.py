# [문제] 두 수를 입력받아 덧셈을 출력하도록 하시오.
# [입력] 4 7      # scanf("%d %d", &n1. &n2)
# [출력] 11

# 공책에 정리하기
n1,n2=map(int, input().split())
# input으로 입력받는 것은 문자열이고 split을 호출하여 쪼갠다
print(n1+n2)

# n1=input(input())   # 이 방법으로는 4와 7을 한 줄에 입력 받을 수 없음.
# n2=input(input())
# print(n1+n2)



# [문제] 두 수를 한 줄에 입력받아 SWAP하여 출력하도록 하시오.
# [입력] 9 7
# [출력] 7 9

a,b=map(int, input().split())
print(a, b)
a, b = b, a     # 두 변수의 값을 교환
print(a, b)