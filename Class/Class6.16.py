bar = [10, 20, 30]

print(bar)

def foo(arg_list):
    arg_list[0] = 100
    
foo(bar)

print(bar)