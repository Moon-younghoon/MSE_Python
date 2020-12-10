import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
# 다음 문자열을 출력해 주기 위해서 변동푝과 시가,최고가를 정의해 주어야함
# 따라서 변동폭은 btc(비트코인)의 최고가-최저가다. 시가는 24시간 내 시작 거래금액이다. 등을 지정해 준다.
#float는 소수점을 위해서 설정해 둔다.
#시가+변동폭이 최고가보다 높으면 상승장, 그렇지 않으면 하락장이라는 것을 출력시키고 싶다.
#if else의 조건문을 활용할 수 있을 것이다.
#정의된 시가와 변동폭, 최고가를 이용해 if문을 작성한다.
#아니면 하락장이라는 문자열을 출력해야 하기 때문에 else를 이용한다.