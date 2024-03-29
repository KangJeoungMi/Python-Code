# 변수 사용하기

# 1. 삼성전자라는 변수로 50,000원을 바인딩해보세요. 
#    삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

삼성전자 = 500000
평가금액 = 삼성전자 * 10
print(평가금액)

# [결과] 5000000

# 2. 다음 표는 삼성전자의 일부 투자정보입니다. 
#    변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
   
시가총액 = 298000000000
현재가 = 50000
PER = 15.79
print(type(시가총액)) # type : int,float, double 등 변수를 알려준다
print(type(현재가))
print(type(PER))

# [결과]
# <class 'int'>
# <class 'int'>
# <class 'float'>

# 문자열 출력

# 3. 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다. hello! python으로 출력해보기

s = "hello"
t = "python"
print(f'{s}! {t}.')

# 4. 2 + 2 * 3 의 실행결과 
print(2+2*3) # 8

# type 함수

# 5. type() 함수는 데이터 타입을 판별합니다. 
#    변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
#    >> a = "132" 의 바인딩된 값의 타입 알아보기

a = 128
print (type(a))
# [결과] <class 'int'>
a="128"
print(type(a))
# [결과] <class 'str'>
