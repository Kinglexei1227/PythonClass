# 공백을 기준으로 문자열에서 특정 단어의 출현 빈도 계산하기

# 총 2번 입력, 첫 번째 입력 = 전체 문자열 검사 , 2 번째 = 단어 출현 빈도
# 사용자로부터 문자열 입력 받기
string = input("문자열 입력: ")

word = input("단어 입력: ")

# 카운트 변수 초기화
count = 0

for _ in word :
    if string == word:
        count += 1
# 결과 출력
print(f"단어 '{word}'의 출현 빈도: {count}")