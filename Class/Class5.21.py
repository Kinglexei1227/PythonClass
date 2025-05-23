
# iteration : 순회
bar = [10, 20, 30, 40, 50]

idx = 0
for val in bar:
    print(f"{idx} index : {val}")
    idx += 1

for idx, val in enumerate(bar):
    print(f"{idx} index: {val}")

# [Unpacking]
pos, kin, sol  = [2, 3, 4]

print(pos, kin, sol)
# 0 index : 10
# 1 index : 20

