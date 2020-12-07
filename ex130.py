import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] # 비트코인의 가격 정보를 가져오는 코드
#btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저
#가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승
#장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.
print(btc)

# float를 사용한 이유는 문자열을 실수로 변환해주어 더하기가 가능해지기 떄문이다.
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])


if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")