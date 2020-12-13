class 예금주:  # 예금주 클래스를 만듦
    def __init__(self, name, balance):
        self.deposit_log = [] # self.deposit_log는 self에 저장되고 리스트로 저장된다.
        self.withdraw_log = [] #self.withdraw_log는 self에 저장되고 리스트로 저장된다.
        self.balance = balance 


    def deposit(self, amount): # 입금을 할수 있는 사용자 정의 함수를 만든다.
        if amount >= 1: # 입금할 경우 음의 값을 입금할 수 없으므로 1이상이어야 한다.
            self.deposit_log.append(amount) # self에 입금한 값을 추가해준다.
            self.balance += amount # balance에 입금한 값을 더해준다.



    def withdraw(self, amount): # 출금을 할수 있는 사용자 정의 함수를 만든다.
        if self.balance > amount: # 출금을 한경우 balance의 값보다 높으면 출금이 불가능하므로 옆의 조건을 건다.
            self.withdraw_log.append(amount) # self에 출금한 값을 추가해준다.
            self.balance -= amount # balance에 출금한 값을 빼준다.


    def withdraw_history(self): # 출금 기록을 확인할수 있는 사용자 정의 함수를 만든다.
        for amount in self.withdraw_log: 
            print(amount) # self.withdraw_log의 입력된 값이 있으면 그 값을 출력하게한다.

    def deposit_history(self): # 입금 기록을 확인할수 있는 사용자 정의 함수를 만든다.
        for amount in self.deposit_log:
            print(amount) # self._log의 입력된 값이 있으면 그 값을 출력하게한다.


k = 예금주("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()