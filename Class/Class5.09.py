foo = [10, 20, 30, 50]

pos = foo
pos[3] = 200

print(foo[3])


# foo = [10, 20]       # 리스트 생성, 요소는 0개 -> 즉 빈 리스트 생성
# pos = list((10, 20)) # 리스트 생성, 요소는 0개 -> 즉 빈 리스트 생성

# foo.append(10) 
# pos.append(20)

# print(foo[0], "\t", pos[0])

# bar = [50, 10, 30, 40, 20]

# for index in range(5):
#     print(bar[index], end=",\t")

# bar[0] = 200
# bar[4] = 100

# print(bar)