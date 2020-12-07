fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?") # input을 사용하여 user의 입력값을 받아줍니다.
if user in fruit.values(): # user가 입력한 값(value)이 fruit에 존재할 경우 아래의 문자열이 출력되고.
    print("정답입니다.")  
else:
    print("오답입니다.") # user가 입력한 값(value)이 fruit에 존재하지 아닐 경우 이 값이 출력됩니다.