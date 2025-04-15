# 키보드로부터 3개의 정수를 입력받아 평균을 계산하는 프로그램을 작성

#사용자로부터 정수 3개를 입력받는다.
input_value1 = int(input("정수 1 입력: "))
input_value2 = int(input("정수 2 입력: "))
input_value3 = int(input("정수 3 입력: "))

#입력받은 3개의 정수의 평균을 계산
average = (input_value1 + input_value2 + input_value3) / 3

#print 함수를 사용하여 평균계산값을 출력
print(f"{average}")