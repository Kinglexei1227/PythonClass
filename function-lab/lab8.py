def calculate_average(*args):
    sum = 0
    for num in args:
        sum += num
    avg = sum / args
    return sum , avg


print(calculate_average(70, 80, 90))