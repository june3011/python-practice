# 2-2) 람다와 map 함수

# map의 첫 번째 인자로 함수가 들어간다면
# 이름 없는 함수 즉, 람다 함수도 가능하다는 뜻 아닙니까?
# 만약에 map의 인자로 사용할 함수가 일회성이거나 매우 짧은 경우에는
# 람다 함수를 사용해서 넘기는 것이 좀 더 효율적 일 것입니다.

# map 과 lambda

# 일반 함수 이용
def func_mul(x):
    return x * 2

result1 = list(map(func_mul, [5, 4, 3, 2, 1]))
print(f"map(일반함수, 리스트) : {result1}")

# 람다 함수 이용
result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1]))
print(f"map(람다함수, 리스트) : {result2}")


# map(일반함수, 리스트) : [10, 8, 6, 4, 2]
# map(람다함수, 리스트) : [10, 8, 6, 4, 2]