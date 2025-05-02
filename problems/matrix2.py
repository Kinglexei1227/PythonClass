# 2단계

# 랜덤설정
import random
# 사용자로부터 입력값 받기
table = int(input("테이블 개수 입력: "))
row = int(input("행 수 입력: "))
col = int(input("열 수 입력: "))
# 메뉴
menu = int(input('''
출력 옵션을 선택하세요:
1. 1부터 시작하여 열 방향으로 증가
2. 1~100 사이랜덤 값 출력                 
옵션 (1 또는 2): '''))
# 반복 설정
# 1번 옵션
for i in range(1, table+1):
    if menu == 1:
        for f in range(row):
            for f in range(col):
                print(f, end=" ")
                
            print()
        print()
# 2번 옵션
    elif menu == 2:
        for a in range(row):
            for a in range(col):
                print(random.randint(1,100), end=" ")
            print()
        print()