
# Map (Dictionary)
bar = {"2523023": "홍길동",
       "2523024": "김철수",
       "2523025": "김영희"} # key 값


print(bar["2523023"])
print(bar["2523024"])
print(bar["2523025"])

print(hash("2523023"))
print(hash("2523024"))
print(hash("2523025"))


# def foo (**kwargs): # 매개변수는 가변 키워드 인자로 오직 하나
#     pass

# foo(a = 2, b = 3, c = 4)
# foo(d = 70, e = 80, f = 90 , g = 100)

# 가변인자 -> *args
# 가변 키워드 인자 -> **kwargs      k = keywords

    
# def 함수 (positional argument, variant arguments,
#           keyword arguments, variant keyword arguments):
#       pass


# def bar(a, *b, c = 20, d = 30 , e = 40):
#     print(a, b, c, d, e)
# # *b 가변인자

# bar(1, 2, 3, 4, 5, 6, 7, 8, 9)
