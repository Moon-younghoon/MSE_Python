ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
 total_profit=0
 
 for day_price in ohlc[1:]:
     profit=day_price[0]-day-price[3]
     total_profit += profit
print(total_profit)




#수익금=시가-종가
#총 수익금을 구해야 함
#total_profit을 0으로 우선 설정, 누적시킬것이다
#매일의 거래일의 시가,종가를 나타내기 위해 변수 day_price설정
#첫번째 날의 시가-종가값을 구하고 total_profit에 누적, 둘째 날의 시가-종가값을 구하고 total_profit에 누적된다.셋째 날도 마찬가지이다
#누적된값을 print함수를 이용해 출력한다.
