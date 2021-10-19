# 함수의 매개변수 사용해보기

def Hello0(name):
    print('Hi', name)

Hello0('Ki')


def Hello1(name):
    print(f'hello, {name}') # f-string 방식으로 출력, f 접두사
    # python 3.6 version 이상

Hello1('kI')


def Hello2(name, hobby):
    print(f'Hi, My name is {name},' \
          f' My hobby is {hobby}')
    # 여러줄 연결 (\)

Hello2('KI', 'sing')


# [문제] 매개변수로 넘긴 문자열 3개를 출력하는 프로그램을 만들어보시오.
def Three(fruit, taste, shape):
    print(f'fruit`s name is {fruit}, fruit`s taste is {taste}, fruit`s shape is {shape}')

Three('apple', 'sweet', 'circle')

# 공책에 적기
def info(name, address, phone):
    print(f'제 이름은 {name}이고요, 제 집주소는 {address}이고, 제 전화번호는 {phone}입니다')
info('기준','대구광역시','010-1234-5678')
# [참고] https://www.python.org.dev/peps/pep-0498/    f-string

# [기초 문제] Hello()함수에 'KIM'이라는 매개변수 값을 넘겨줄 때
# 'Hi,kim'이 출력되도록 하시오.
# Hello('KIM')

def Hello(name):
    print(f'Hi, {name}')

Hello('KIM')


# [기초 문제] 나이와 이름을 입력받고 출력하는 프로그램을 만드시오.
def HHello(name, age):
    print(f'Hi, {name}, You are {age} years old')

name=input('이름 : ')
age=input('나이 : ')
HHello(name,age)


# [문제] 자신이 좋아하는 가수 이름을 3개 입력(input())받고, 출력하는 함수 만들기
# 함수 이름 : singer(a,b,c)
def singer(a ,b ,c):
    print(f'내가 좋아하는 가수 {a},{b},{c} 입니다.')
    # print('내가 좋아하는 가수', a, b, c, '입니다')

a=input('좋아하는 첫 번째 가수 : ')
b=input('좋아하는 두 번째 가수 : ')
c=input('좋아하는 세 번째 가수 : ')
singer(a, b, c)
