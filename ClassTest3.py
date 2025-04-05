#전역 변수 count=0 선언
count = 0
#increase 함수 정의 (전역 변수 count를 1 증가)
def increase():
    global count
    count += 1
#increase() 함수 여러 번 호출
increase()
increase()
#최종적으로 count 출력
print(f"최종 count:{count}")
