if True :
    if False: # False가 아니므로 1, 2는 출력되지 않는다.
        print("1")
        print("2")
    else: # 위의 조건이 맞지 않으므로 3이 출력된다.
        print("3")
else : # 위의 값이 참이므로 출력이 되지 않는다.
    print("4")
print("5") #위의 조건에 관계없이 5가 출력된다.