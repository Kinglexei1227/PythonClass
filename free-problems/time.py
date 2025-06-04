# 사용자로부터 입력 받기
time_hour = int(input("출발 시 (시간)을 입력하세요: "))
time_minute = int(input("출발 시 (분)을 입력하세요: "))
arrive_hour = int(input("도착 시 (시간)을 입력하세요: "))
arrive_minute = int(input("도착 시 (분)을 입력하세요: "))
distance = int(input("이동 거리(km)를 입력하세요: "))

# 이동 거리 와 평균 속도 수식
avg_speed = distance / (arrive_hour - time_hour) + ((arrive_minute - time_minute) / 60)

if avg_speed < 60:
    speed = "느림"
elif 60 <= avg_speed < 90:
    speed = "보통"
else:
    speed = "빠름"

# 결과 출력
print(f'''
이동 거리: {distance}
출발 시간: {time_hour}시 {time_minute}분
도착 시간: {arrive_hour}시 {arrive_minute}분
평균 속도: {avg_speed}km/h
속도 상태: {speed}    
      ''')