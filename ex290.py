class 부모: # 
    def __init__(self):
    print("부모생성")

class 자식(부모): 
    def __init__(self): 
    print("자식생성")
    super().__init__() # super를 이용하면 부모 클래스에 접근이 가능함

나 = 자식() # 자식 클래스가 먼저 호출이 되어 "자식생성"이 먼저 호출된다. 그리고 나서 super 로 인해 부모 클래스에 접근이 되어 "부모생성"이 출력된다.