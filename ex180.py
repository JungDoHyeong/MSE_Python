low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [] # 리스트에 저장한다.
for i in range(len(low_prices)) : # 변수 범위 설정 5개 
    volatility.append(high_prices[i] - low_prices[i]) # append함수를 이용하여 추가하고 싶은 값을 넣어줄 수 있다.


