# 도서관 검색대 프로그램
# 사용자로부터 제목 입력받기

# 빈 리스트 생성
books = []

# 사용자 입력을 처리하는 루프 시작
while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    if title == '종료':
        break
    else:
        books.append(title)


# 최종 도서 목록을 출력
print("도서 목록:", books)