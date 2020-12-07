per = ["10.31", "", "8.00"]

for i in per: 
    try: # try를 통해 10.31이 정상적으로 작동하여 cleand ata 와 변환 완료가 출력
         # try를 통해 아무것도 출력이 되지 않아 0이 출력되고 변환 완료가 출력
         # try를 통해 8.00이 정상적으로 작동하여 clean data와 변환 완료가 출력이 된다.   
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")