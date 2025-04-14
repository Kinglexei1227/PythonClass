# 학생의 점수를 기반으로 우수합격/합격/불합격 판정을 내리는 프로그램.

# 사용자로부터 국어, 영어, 수학 점수를 입력받는다. (정수형)

korean_score = int(input("국어 점수: "))
english_score = int(input("영어 점수: "))
math_score = int(input("수학 점수: "))


# 입력받은세 과목의 점수를 이용해 평균을 계산. 평균 계산식: (국어점수 + 영어점수 + 수학점수) / 3 
avg = (korean_score + english_score + math_score) / 3

# 평균 점수를 소수 첫째 자리까지 출력
print(f"평균: {avg:.1f}")
# 조건에 따라 결과 판정 (if조건문문)
# 평균이 90 이상이고 각 과목이 80점 이상이면 -> "결과: 우수 합격" 출력
if avg >= 90 and korean_score >= 80 and english_score >= 80 and math_score >= 80:
    print("결과: 우수 합격")
# 평균이 70이상이고 각 과목이 모두 40점 이상이면 -> "결과: 합격" 출력
elif avg >= 70 and korean_score >=40 and english_score >= 40 and math_score >= 40:
    print("결과: 합격")
# 그 외에는 -> "불합격" 출력
else :
    print("결과: 불합격")
