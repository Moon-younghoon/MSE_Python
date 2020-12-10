date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table=dictzip((date, close_price))
# 리스트 두개를 한개의 딕셔너리로 바꿔주어야 함
# zip을 이용하여 date 와 close_price 두개의 list를 묶어준다
#zip을 거친 date와 close_price는 0번끼리,1번끼리...4번끼리 묶이게 된다
#이렇게 묶인 값들을 dict를 이용해 딕셔너리로 바꿔준다.
# 바꿔준 값을 close_table 로 새롭게 정의해준다.