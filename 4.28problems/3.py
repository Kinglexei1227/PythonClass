# for 문을 사용하여 아래 문자열 내 "h"의 개수를 출력하는 프로그램 작성

myString = "hello hyundai hoho"

count = 0

for i in myString:
    if i == "h":
        count += 1

print(f"문자열 내 h 갯수 :{count}")