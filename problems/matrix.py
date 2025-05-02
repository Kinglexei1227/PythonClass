# 사용자로부터 테이블 개수, 테이블의 행 수, 열 수를 입력 받아 *로 구성된 테이블과 테이블 개수를 출력하라.

# 사용자로부터 입력값 받기
T = int(input("테이블 개수 입력: "))
M = int(input("행 수 입력: "))
N = int(input("열 수 입력: "))


# 매트릭스 생성 반복문
for i in range(T):
    for a in range(M):
            print("*" * N)
    print()