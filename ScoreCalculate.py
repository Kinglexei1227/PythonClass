#학생들의 세 과목 점수를 입력받아 평균 점수를 계산하고,
#평균에 따른 학점 등급을 부여하는 프로그램을 만듭니다.

#사용자로부터 수학, 과학, 영어의 점수를 입력받습니다.
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

#입력받은 점수들은 바탕으로 평균 점수를 계산합니다.
def calculate_average(math_score, science_score, english_score):
    return (math_score + science_score + english_score) / 3

#계산된 평균 점수를 사용하여 학점 등급을 결정합니다.
def get_grade(average):
    if average >= 90:
        return "A" 
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
#평균계산 함수호출
average = calculate_average(math_score, science_score, english_score)
#학점 등급계산 함수호출
grade = get_grade(average)
#계산된 평균점수 결과 와 학점 등급 결과출력
print(f"평균 점수는 {average}점이고, 학점은{grade}입니다.")