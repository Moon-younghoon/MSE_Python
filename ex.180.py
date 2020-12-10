low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(5):
    volatility.append(high_prices[i] - low_prices[i])
# 변동폯=고가-저가, 위 값을 volatility라는 list에 저장해 주어야 함
# 문제에 나온 low_prices와 high_prices를 그대로 정의
#volatility를 리스트로 정의해준다.
#0,1,2,3,4번의 변수로 정의하면 각각의 값에 접근해 줄수 있기 때문에 for 문과 range함수를 사용하여 i를 정의해준다.
#리스트인 volatility값에 list method인 append를 사용해 첨가해준다.
#volatility는 변동푝이기 때문에 high_prices[i]-low_prices[i]값을 첨가해준다
