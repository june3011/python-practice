# 파이썬 필터와 맵 예제

# 1-2 map 함수를 사용하는 것과 아닌 것의 차이
# 똑같은 작업을 map을 이용했을 때와 그렇지 않을 때를 비교하겠습니다.


# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1=[]
for val in myList:
    result1.append(val+1)

print(f'result1 : {result1}')

# map 함수 이용
def add_one(n):
    return n+1

result2 = list(map(add_one, myList))    # map반환을 list로 변환
print(f'result2 : {result2}')

# result : [2, 3, 4, 5, 6]
# result : [2, 3, 4, 5, 6]