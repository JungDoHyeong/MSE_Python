def print_max(a, b, c) : 
    max_val = 0
    if a > b and a< c : # a를 b와 c에 비교하여 둘다 참일 경우 a 출력  
        print(a)
    elif b > c and b<a : # b를 a와 c에 비교하여 둘다 참일 경우 B출력
        max_val = b
    else:
        print(c) # 위의 두조건이 모두 만족하지 않으면 c가 출력된다.