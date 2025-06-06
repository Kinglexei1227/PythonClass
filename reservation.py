# 사전 예약 시스템의 로직을 시뮬레이션하는 프로그램을 작성.
# 이 시스템은 사용자가 특정 입네트의 사전 예약을 진행 할때, 사용자의 입력에따라
# 예약 가능 여부를 판단하고 그에 따른 결과를 출력하는 프로그램 작성.

# 사용자에게 다음 정보를 입력받습니다.
age = int(input("나이를 입력하세요: "))
#각 이벤트 코드별로 다음과 같은 규칙을 적용.
# 사용자로부터 입력 받는 이벤트 코드는 'E1','E2','E3' 중 하나입니다.
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")

reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 사용자로부터 받은 입력값의 형식 검사
# 사용자로부터 받은 입력값이 정해진 형식에 맞지 않을경우 "잘못된 입력입니다. 프로그램을 종료합니다." 출력 후,
# 프로그램을 종료
if not event_code in ['E1', 'E2' ,'E3'] :
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    exit()
if not (1 <= reservation_date <= 30) :
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    exit()
# 이벤트 코드에 따른 예약 조건 체크
if event_code == 'E1': #E1 을 선택시 나이는 18세이상만 예약가능.
    if age < 18 :
        print("나이 제한으로 인해 예약할 수 없습니다.")
    else:
        print("예약이 완료되었습니다!")

elif event_code == 'E2': #E2 를 선택시 날짜는 짝수일에만 예약가능.
    if reservation_date % 2 != 0 :
        print("선택하신 날짜에는 예약할 수 없습니다.")
    else:
        print("예약이 완료되었습니다!")
elif event_code == 'E3': #E3 를 선택시 나이는 16세 이상, 7의 배수은 날짜에만 예약가능.
    if age < 16 :
        print("나이 제한으로 인해 예약할 수 없습니다.")
    elif reservation_date % 7 != 0 :
        print("선택하신 날짜에는 예약할 수 없습니다.")
    else:
        print("예약이 완료되었습니다!")
