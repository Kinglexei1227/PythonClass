# for 문을 통해 문자열 내 단어 개수를 출력 하는 프로그램을 작성

myString = "It is a great weather with you"

count = 1

for char in myString:
    if char == " ":
        count += 1 # 공백 + 1
# 단어 개수 출력
print(f"문자열 단어 갯수 : {count}")