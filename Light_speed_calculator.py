
# 사용자로부터 거리를 킬로미터 단위로 입력받습니다.
Distance = int(input("여행할 거리를 킬로미터(km) 단위로 입력하세요: "))

# 빛의 속도는 초당 299,792킬로미터입니다.
Light_speed = int(299792)

# 빛이 해당 거리를 여행하는 데 걸리는 시간을 계산하여 화면에 출력합니다.
Tour_Distance = Distance / Light_speed
print ("빛이", Distance, "킬로미터를 여행하는데 걸리는 시간은", Tour_Distance, "초입니다.")