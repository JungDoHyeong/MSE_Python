date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))# dict을 이용하여 딕셔너리를 생성하고 zip함수를 사용하여 쌍을 지어서 묶어준다.
print(close_table)