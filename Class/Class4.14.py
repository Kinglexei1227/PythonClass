# 점수를 입력 받아
# 입력 점수가 0보다 작으면
# " 입력 값 오류" 출력 후 
# 프로그램 종료
score = int(input("점수 입력: "))
# 입력 값이 0 미만일 경우 에러 메세지 출력 후 프로그램 종료
if score < 0 :
    print("입력 값 오류")
# 입력 값이 0 이상일 경우 합격 여부 판단.
else:

# if-else: 점수가 80점 이상이면 "합격"
# 아니면 "불합격"

    if score >= 80 :
        print("합격")
    else :
        print("불합격")
        
    # if-elif-else:
    # 점수에 따라 등급 부여 (90점이상 A, 80 B , 70 C, 그 외 D)
    if score >= 90 :
        print("A")
    elif score >= 80 :
        print("B")
    elif score >= 70 :
        print("C")
    else :
        print("D")
        
if score >= 95 :# 중첩 if: A등급이면서 동시에 95점 이상이면
    print("우수상")# "우수상" 출력
if score == 100 : # 추가 조건: 점수가 100이면
    print("만점 축하!") # "만점 축하!" 출력
    
    