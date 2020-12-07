ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100], # 수익금 0원 
        [200, 210, 180, 190], # 수익금 -10원
        [300, 310, 300, 310]] # 수익금 10원

total = 0
for day in ohlc[1:]: 
    profit = day[3]- day[0] # 시가[0]에 사고 종가[3] 에 팔았으므로 식은 옆과 같다. 
    total+= profit # 3일동안의 수익금을 더해준다.
print(total)    