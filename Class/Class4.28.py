# count = 0
# while count < 3:
#     for value in range(1, 3):
#         if count == 1:
#             continue
        
#         print("count : ", count, ", value :", value)
        
#     count += 1

row = int(input("별 개수: "))

for num_row in range(1, row + 1):
    # " " 반복
    for _ in range(row - num_row):
        # " " 출력
        print(" ", end="")
    
    # "*" 반복
    for _ in range(num_row):
        # "*" 출력
        print("*", end="")
        
    print()
    