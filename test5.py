if 3 < 2 and 3 < 3:
    print("형")
    
if 3 > 2 and 3 < 3:
    print("보")
    
if 3 < 2 and 3 >= 3:
    print("수")

if 3 > 2 and 3 >= 3:
    print("지")

# if 3 < 2 or 3 < 3:
#     print("T 1")

# if 3 > 2 or 3 < 3:
#     print("T 2")
    
# if 3 < 2 or 3 >= 3:
#     print("T 3")
    
# if 3 > 2 or 3 >= 3:
#     print("T 4")

# if not (2 > 3):
#     print("T 1")
# else:
#     print("F 1")
    
# if not (2 < 3):
#     print("T 1")
# else:
#     print("F 2")

def returnNum(argNum):
    print("argNum: ", argNum, "\treturnNum () is voked")
    return argNum

returnNum(1)


if True and returnNum(2) == 2:
    print("True")
    
    
if False and returnNum(3) == 2:
    print("True")
    

if True or returnNum(4) == 4:
    print("True")
    
    
if False or returnNum(5) == 4:
    print("True")