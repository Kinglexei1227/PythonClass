# while 문을 사용하여 1~1000 까지의 정수 중 3의 배수의 총합을 구하기

count = 1
total = 0
while count <= 1000:
    if count % 3 == 0:
        total += count
    count += 1

print(f"1~1000 사이 정수 중 3의 배수의 총 합은 :{total}")