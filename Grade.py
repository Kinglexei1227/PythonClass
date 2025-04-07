# 대학에서의 출석 점수 계산 프로그램 작성

# 출석점수 계산법.
# 20점에서 결석시간에 비례하는 점수를 차감합니다
# 계산식: 20 - (20 * 결석시간 수 /총 수업시간수)

# 총 수업 시간 계산법: 시수/주 x 15

# 지각 처리 규칙: 결석시수가 총수업시수의 1/4을 초과할 경우 학점 미부여 (F처리)

# 사용자로부터 주당 수업 시간(시수/주), 결석한 총 시간, 지각 횟수를 입력 받습니다.
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

# 출석 점수 계산
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    hours_per_week 