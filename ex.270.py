종목 = []
#종목을 list로 정의
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
# 삼성전제,현대차,LG전자의 종목코드,PER,PBR,배당수익률을 정의
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
#종목이라는 list안에 append method사용하여 삼성,현대차,LG전자를 삽입

for i in 종목:
    print(i.code, i.per) 
#;for loop를 돌림 i는 삼성 현대차 LG전자가 될 것이다.
#stock 클래스의 객체를 바인딩, 따라서 코드는 i.code, PER은 i.per로 출력할 수 있따.
  