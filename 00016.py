# 2-2) filter 함수와 람다 함수

# filter 함수의 처 번째 매개변수에 함수가 들어오는데,
# 간단한 함수 거나 한 번만 사용하는 일회성 함수인 경우
# 따로 def를 이용해서 함수를 만들기보다는
# lambda 함수를 이용해서 함수를 만드는 것이 좀 더 편리할 수 있습니다.


arr = [1, 10.2, 100.3, 2.3, 20.2, 200.3, 3, 30, 300]

result1 = list(filter(lambda n : n < 10, arr))
result2 = list(filter(lambda n : isinstance(n, int), arr))
result3 = list(filter(lambda n : isinstance(n, float), arr))

print(f'원래 리스트 : {arr}')
print(f'10보다 작은 수 : {result1}')
print(f'정수만 출력 {result2}')
print(f'실수만 출력 {result3}')


# 원래 리스트 : [1, 10.2, 100.3, 2.3, 20.2, 200.3, 3, 30, 300]
# 10보다 작은 수 : [1, 2.3, 3]
# 정수만 출력 [1, 3, 30, 300]
# 실수만 출력 [10.2, 100.3, 2.3, 20.2, 200.3]