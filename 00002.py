# 10진수를 oct 내장 함수(8진수 변환), hex 내장 함수(16진수 변환), bin 내장 함수(2진수 변환)

# 0으로 채우는 zfill
# Fill the string with zeros
n=20
print(hex(n))   # 0 x 14

n=str(hex(n))
print(n.zfill(10))

n1=str(30)
print(n1.zfill(10))

n2='hello'
print(n2.zfill(10))