for value_1 in range(2): # 0, 1
    for value_2 in range(2):
        
        for value_3 in range(2):
            if value_3 == 1:
                break
            
            print(f"{value_1} {value_2} {value_3}\t", end="")
        
        print()
    print()