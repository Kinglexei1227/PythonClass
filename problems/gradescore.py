# 학생들의 점수 데이터를 분석하여, 점수에 따른 등급 분포를 텍스트 기반의 그래프로 시각화하는 프로그램을 작성

scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

# 점수 등급 분류
grades = {
    "A" : [],
    "B" : [],
    "C" : [],
    "D" : [],
    "F" : [],
}

# 점수를 반복하면서 등급 분류
for score in scores :
    if score >= 90 :
        grades["A"].append(score)
    elif score >= 80 :
        grades["B"].append(score)
    elif score >= 70 :
        grades["C"].append(score)
    elif score >= 60 :
        grades["D"].append(score)
    else :
        grades["F"].append(score)

# 결과 출력
print("등급 분포 및 평균 점수: ")
for grade in ["A","B","C","D","F"]:
    student_scores = grades[grade]
    count = len(student_scores)
    if count > 0:
        avg = sum(student_scores) / count
        print(f"{grade} 등급: 평균 점수 = {avg:.2f}")
    else:
        print(f"{grade} 등급: 평균 점수 = 없음")
    print("*" * count + f" ({count}명)")
    