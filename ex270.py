class Stock: #Stock 클래스를 생성하여 객체가 생성될 때 종목명과 종목코드, PER, PBR 배당수익률을 입력 받을수 있도록  생성자를 정의 함
    
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

종목 = [] # 리스트를 생성하여 리스트에 저장한다.

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성) # append함수를 이용하여 종목에 생성된 객채를  넣어준다.
종목.append(현대차)
종목.append(LG전자)

for i in 종목: # i= 삼성 일 때 코드와 per 입력 , i= guseock 일 때 코드와 per 입력, i= LG전자 일 때 코드와 per 입력
    print(i.code, i.per)      