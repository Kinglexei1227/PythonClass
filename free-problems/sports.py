# 사용자로부터 온도 입력 받기
user_input = float(input("현재 온도(섭씨)를 입력하세요: "))

# 조건문
if user_input < 10:
    sports = "스키"
elif 10 <= user_input < 20:
    sports = "자전거 타기"
elif 20 <= user_input < 30:
    sports = "등산"
else:
    sports = "수영"

print(f"현재 온도: {user_input}도")
print(f"추천 활동: {sports}")