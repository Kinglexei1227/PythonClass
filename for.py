# 구구단
# 2 * 1 =2, 2 * 2 = 4 ....... 2 * 9 = 18
#
# ....................9 * 9 = 81


# 단 : 2, 3, 4, ..... 9
# for dan in range (2, 10, 2):
#     # 1 ~ 9 숫자 (for중첩)
#         for num in range(1, 10):
#             print(f"{dan} X {num} = {dan * num}")
#         print("")
word = input("단어를 입력하세요: ")
count = 0

for _ in word :
    count += 1

print(f"입력 단어 {word}의 길이는 {count}")