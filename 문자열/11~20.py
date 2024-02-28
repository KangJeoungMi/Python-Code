# 011 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

letters = 'python'
print(letters[0],letters[2])

# 012 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
car_num = "24가 2210"
print(car_num[4:]) 
# print(car_num[-4:])

# 013 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
String = "홀짝홀짝홀짝"
print(String[::2])
# [::N] (이중콜론) = 리스트 전체에서 인덱스 0부터 N씩 증가시키면서 가져옴

# ⭐⭐ 014 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
String = "PYTHON"
print(String[::-1])

# 015 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))

# 016 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(phone_number.replace("-",""))

# 017 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

url = "http://sharebook.kr"
print(url[-2:])