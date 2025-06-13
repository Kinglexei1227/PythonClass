sol = {"a" : 10, "b" : 20, "c" : 30}

for key , item in sol.items():
    print(f"Key: {key}, Item: {item}")




bar = {"std1" : 10, "std2" : 20, "std3" : 30 }

# read
print(bar.pop("std4", False))
print(bar)

# print(bar["std1"])
# print(bar["std4"])
# print(bar.get("std5", False))


# create
# if bar.setdefault("std4", 200) == 200:
#     print("입력 성공")
# else:
#     print("입력 실패")
    
# print(bar.setdefault("std1", 100))
# print(bar)