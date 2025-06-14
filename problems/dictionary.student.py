posts = [
    {"title": "첫 글", "author": "철수", "content": "안녕하세요"},
    {"title": "두 번째 글", "author": "영희", "content": "반가워요"},
    {"title": "세 번째 글", "author": "민수", "content": "공지입니다"}
]

# 예: 첫 번째 글의 제목 출력
print(posts[0]["title"])  # 첫 글

# 예: 모든 글 출력
for post in posts:
    print(f"{post['title']} - {post['author']}: {post['content']}")
