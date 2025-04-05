# 사용자로부터 left, right, up, down 중 하나의 단어를 입력받아
# 입력받은 문자열에 따라 ("왼쪽" "오른쪽" "위" "아래") 로 이동합니다.
# 를 입력받는 프로그램을 작성.

#사용자에게 방향을 입력받습니다.
Direction = input("방향을 입력하세요(left, right, up, down)")

#입력받은 방향에 따른 메시지를 결정합니다.
if Direction == "left" :
    print("왼쪽으로 이동합니다.")
elif Direction == "right" :
    print("오른쪽으로 이동합니다.")
elif Direction == "up" :
    print("위로 이동합니다.")
elif Direction == "down" :
    print("아래로 이동합니다.")
else :
    print("알 수 없는 명령입니다.")
#메시지를 출력합니다.