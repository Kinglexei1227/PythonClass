# 사용자로부터 하나의 영문자를 입력받고 
# 해당 문자가 모음(a, e, i, o, u) 중 
# 하나인지 아닌지를 판별하여 결과를 출력하는 프로그램을 작성하세요.

#사용자에게 하나의 문자를 입력받습니다.
Alphabet = input("한 문자를 입력하세요")
vowel = "aeiou"
#입력받은 문자가모음인지 아닌지 확인합니다.
for char in Alphabet :
    if char in vowel :
        print(Alphabet,"는 모음입니다.")
    else :
        print(Alphabet,"는 모음이 아닙니다.")
#결과를 출력합니다.
