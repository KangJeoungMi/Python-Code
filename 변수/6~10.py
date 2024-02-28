# 문자열을 정수로 변환

# 6. 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
num_int = int(num_str)
print(num_int,type(num_int))
# [결과] 720 <class 'int'>

# 정수를 문자열 100으로 변환
# 7. 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
num_string = str(num)
print(num_string,type(num_string))

# [결과] 100 <class 'str'>


# 문자열을 실수로 변환
# 8. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

num1 = "15.79"
numf = float(num1)
print(numf, type(numf))

# [결과] 15.79 <class 'float'>

# 9. year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 
#    이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

year = "2020"
print(int(year)+1) # 2021
print(int(year)+2) # 2022
print(int(year)+3) # 2023

# 10. 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 
#     총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
aircon = 48584
price = aircon*36
print(price) # 1749024