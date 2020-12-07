def message1(): # def 사용자 정의 함수로 message1()을 입력하면 A가 출력된다.
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) : # i = 0일 때 B,C 출력 i = 1일 때 B,C 출력 i = 2일 때 B,C 출력 
        message2() 
        print("C")
    message1() # 마지막으로 A출력이 된다.

message3() # BCBCBCA가 출력된다.