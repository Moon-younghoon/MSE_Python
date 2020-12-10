data="   삼성전자   "
#data는 삼성전자이고 양쪽에 존재하는 공백을 지우고 싶다.
data1=data.strip()
#list method인 strip method를 사용하여 원본 문자열에서의 공백이 없어진 새로운 문자열을 반환시킨다.
print(data1)
# print 함수를 활용하여 공백이 없어진 새롭게 반환된 문자열인 data1 을 출력시킨다.
# 결과값은 "삼성전자"가 나올 것이다.