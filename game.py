import time
import random

# 게임 데이터를 game_name_value_dict에 저장
game_name_value_dict = { 
    #미국 주 맞추기 
    '미국 주 맞추기(중복X)' : [
    '알라바마', '알래스카', '애리조나', '아칸소', '캘리포니아', '콜로라도', '코네티컷', '델라웨어', '플로리다', '조지아',
    '하와이', '아이오와', '아이다호', '일리노이', '인디애나', '캔자스', '켄터키', '루이지애나', '메인',
    '메릴랜드', '매사추세츠', '미시간', '미네소타', '미시시피', '미주리', '몬태나', '네브래스카', '네바다', '뉴햄프셔',
    '뉴저지', '뉴멕시코', '뉴욕', '노스캐롤라이나', '노스다코타', '오하이오', '오클라호마', '오리건', '펜실베이니아',
    '로드아일랜드', '사우스캐롤라이나', '사우스다코타', '테네시', '텍사스', '유타', '버몬트', '버지니아', '워싱턴',
    '웨스트버지니아', '위스콘신', '와이오밍'],
    # 일본 주 맞추기
    '일본 도도부현 맞추기(중복X)' : [
    "도쿄도", "홋카이도", "오사카부", "교토부", "가나가와현", "사이타마현", "치바현", 
    "아이치현", "후쿠오카현", "히로시마현", "효고현", "오키나와현", 
    "나가노현", "미에현", "시가현", "고치현", "야마구치현", "후쿠시마현", 
    "이시카와현", "가고시마현", "도쿠시마현", "오카야마현", "아키타현", 
    "카가와현", "미야기현", "나가사키현", "군마현", "나라현", "와카야마현", 
    "구마모토현", "시마네현", "야마나시현", "토치기현", "사가현", "니가타현", 
    "시즈오카현"],
    #경상도 도시 맞추기
    '경상도 도시 맞추기(중복X)' : [ 
    "포항", "경주", "안동", "구미", "김천", "상주", "영주", "문경", "영천", "칠곡", "고령", "예천",
    "영덕", "울진", "봉화", "의성", "청송", "군위", "울릉", "성주", "청도", "합천", "부산", "창원", 
    "진주", "김해", "양산", "거제", "통영", "밀양", "사천", "함안", "고성", "창녕", "합천", "남해", 
    "의령", "하동", "산청", "거창", "통영"],
    #수도권 도시 맞추기
    '수도권 도시 맞추기(중복X)' : [
    "서울", "인천", "수원", "고양", "성남", "용인", "부천", "화성", "평택", "시흥", 
    "파주", "김포", "광명", "안양", "안산", "광주", "여주", "양주", "동두천", "하남", 
    "오산", "구리", "안성", "포천", "이천", "김포", "양평", "의왕", "군포", "구리", 
    "여주", "연천", "가평", "남양주", "시흥", "파주", "광명", "성남", "용인", "의정부", 
    "하남", "오산", "화성", "평택"]

}

# 깔끔함을 위한 줄 구분 함수 선언
def line():
    print("=====================================")


# 게임 랜덤 선택 함수 선언
def what_game():
    # 게임 랜덤으로 선택
    print("게임을 랜덤으로 선택합니다")
    
    # 현실감을 위해 1초간 대기 후 선택중인 것처럼 .을 출력x3
    for i in range(3):
        time.sleep(1)
        print(".")
    
    # game_name_value_dict에서 랜덤으로 key를 선택
    selected_game_key = random.choice(list(game_name_value_dict))
    
    #현실감을 위해 2초간 대기후 선택된 게임 출력
    time.sleep(2)
    line()
    print(f"선택된 게임은 {selected_game_key} 입니다!")
    line()

    #선택된 key의 value값 리턴하기
    return game_name_value_dict[selected_game_key]
    
#플레이어 닉네임 입력받는 함수 선언
def get_player_nickname(num):
    # 플레이어 수 만큼 닉네임 입력받기 
    for i in range(num):
        nickname = input(f"{i+1}번 플레이어의 닉네임을 입력하세요 : ")
        
        #입력받은 닉네임을 user_list에 dict 타입으로 저장. score 도 시작값 0으로 해서 할당.
        user = { 'nickname' : nickname , 'score' : 0 }
        player_list.append(user)
    line()



#############################################################################

#전역

# 플레이어들을 저장할 리스트 선언
player_list = []


# 플레이어 몇명인지 입력받기
print("안녕하세요 ! Ethan Park의 랜덤 지리 게임에 오신 것을 환영합니다. ")
player_num = int(input("플레이어 수를 입력해주세요 : "))

# 플레이어 닉네임 입력받는 함수 호출
get_player_nickname(player_num)

# 게임 랜덤 선택 함수를 호출하기
Q_list = what_game()

# 플레이어 순서를 랜덤으로 지정해서 리스트에 순서 넣기
random.shuffle(player_list)
ran_player_list = player_list

# 리스트 순서에 따라 Q_list값이 0이 될때까지 게임 진행
while len(Q_list) > 0:
    #플레이어들이 번갈아가면서 답 입력
    for i in range(len(ran_player_list)):
        #만약 입력도중 Q_list내의 값이 0이 되면 반복문 종료
        if len(Q_list) <= 0:
            break
        #아니라면 몇문제 남았는지 알려주고 구분선 함수 호출
        else:
            print(f"{len(Q_list)} 문제 남았습니다.")
            line()
        #답을 입력받기
        temp = input(f"{ran_player_list[i]['nickname']}님이 정답을 입력하실 차례입니다. : ")
        line()

        #만약 입력받은 값이 '점수표'라면 점수표를 출력후 계속해서 정답 받기.
        if temp == '점수표':
            print()
            line()
            temp = input("정답을 다시 입력해주세요. : ")
            line()
        
        #만약 입력받은 답이 Q_list안에 있을경우 Q_list내의 답 제거 후 정답이라고 출력후, player의 score증가
        if temp in Q_list:
            Q_list.remove(temp)
            print(f"{ran_player_list[i]['nickname']}님이 정답을 맞췄습니다! [ +1 점]")
            line()
            ran_player_list[i]['score'] += 1

    
        #입력받은 답이 Q_list안에 없을 경우 오답이라고 출력후 player의 score감소
        else:
            print(" 이미 앞에서 입력했거나 존재하지 않는 답입니다! [-1 점]")
            player_list[i]['score'] -= 1

x = []

for i in range(len(ran_player_list)) :
    x.append(ran_player_list[i]['score'])
    
x.sort(reverse=True) 

count = 0
for i in x :
    for y in range(len(ran_player_list)) :
        if ran_player_list[y]["score"] == i :
            ran_player_list[y], ran_player_list[count] = ran_player_list[count] , ran_player_list[y]
        else : 
            pass
    count += 1

print("게임이 끝났습니다! 점수표를 출력합니다.")
line()
for i in range(len(ran_player_list)) :
    print(f"{i+1}등 : {ran_player_list[i]}")
line()