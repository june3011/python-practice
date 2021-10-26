# 2. map 함수 예제

# 2-1) 리스트와 map 함수

import math # math.ceil 함수 사용

# 예제1) 리스트의 값을 정수 타입으로 변환
result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(int, 리스트) : {result1}')

# 예제2) 리스트 값 제곱
def func_pow(x):
    return pow(x, 5)    # x의 5제곱을 반환

result2 = list(map(func_pow, [1, 2, 3, 4, 5]))
print(f'map(func_pow, 리스트) : {result2}')

#예제3) 리스트 값 소수점 올림
result3 = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]))
print(f'map(func_ceil, 리스트) : {result3}')


# map(int, 리스트) : [1, 2, 3, 4, 5]
# map(func_pow, 리스트) : [1, 32, 243, 1024, 3125]
# map(func_ceil, 리스트) : [2, 3, 4, 5, 6, 7]