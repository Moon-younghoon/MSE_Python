per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))#실수로 변환이 되지 않는것이 발생, 예외가 생김 
    except:
        print(0) #예외가 생긴다면 0을 출력
    else:
        print("clean data")# 예외가 발생하지 않는다면  clean data를 출력
    finally:
        print("변환 완료") 최종적으로 변환완료 출력됨