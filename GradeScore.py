# 사용자로부터 국어, 영어, 수학 점수를 입력받고, 세 과목의 평균점수를 계산.

korean_score = int(input("국어 점수: "))
english_score = int(input("영어 점수: "))
math_score = int(input("수학 점수: "))


# 받은 입력값을 평균계산
avg = (korean_score + english_score + math_score) / 3
# 세 과목의 평균 점수의 학점 판정

# 평균 출력
print(f"평균: {avg:.1f}")
# 판정
if avg >= 90 and korean_score >= 80 and english_score >= 80 and math_score >= 80:
    print("결과: 우수 합격")
elif avg >= 70 and korean_score >=40 and english_score >= 40 and math_score >= 40:
    print("결과: 합격")
else :
    print("결과: 불합격")
