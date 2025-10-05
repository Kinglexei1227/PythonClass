# 전체 학생 정보
std_dict = {}

# 학생 한 명의 정보
std_data = {}


std_data['id'] = int(input("ID를 입력하세요:\t"))
std_data['name'] = input("이름을 입력하세요:\t")
#
#
#

std_dict[std_data['id']] = std_data

print(std_dict[std_data['id']]['name'])