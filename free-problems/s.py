# 일단 이건 필수잔하요
count = int(input())

for i in range(count) :
    k = int(input())
    n = int(input())

    lst = [i for i in range(1,n+1)]
    
    for floor in range(k) :
        lst_2 = []
        for room in range(1, n+1) :
            lst_2.append(sum(lst[:room]))
        lst = lst_2
        
    print(lst[-1])