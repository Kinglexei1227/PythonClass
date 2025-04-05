# 사용자가 제곱미터(m^2) 단위로 입력한 토지의 면적을
# 평방피트(ft^2)와 에이커(ac) 단위로 변환해주는 프로그램을 작성하세요. 
square_meters = float(input("토지의 면적을 제곱미터 (m^2) 단위로 입력하세요: "))

def convert_to_square_feet() :
    global square_meters 
    square_meters = square_meters * 10.7639
    return  square_meters
    
def convert_to_acres():
    global square_meters 
    square_meters = square_meters / 4046.86
    return square_meters

if square_meters < 0 :
    print("잘못된 입력입니다.")

    
acres = convert_to_acres()
square_feet = convert_to_square_feet()
print(f"{square_meters} 제곱미터는 {square_feet} 평방피트입니다.")
print(f"{square_meters} 제곱미터는 {acres} 에이커입니다.")