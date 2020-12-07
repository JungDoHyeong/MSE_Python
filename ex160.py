리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    name, ext = i.split(".") # split 함수를 이용하여 "."을 기준으로 나눈다.
    if ext == 'h' or ext =='c': #논리 연산자 or을 사용하여 'h','c'가 있는지 확인한다. 
        print(i)