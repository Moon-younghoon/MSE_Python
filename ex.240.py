#28
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)
# 조건: 함수2로 정의된 함수 즉 함수2(num)의 num은 num+10 또한 이값은 함수1(num)으로 return된다.
#즉 함수 1(num)은 함수2에서 주어진(num)값에 10을 더해줘야 한다.
#같은 원리로 함수0의 (num)은 함수1의(num)값에 2를 더해줘야한다.
c = 함수2(2)
print(c)
#위와같이 c를 출력해야하므로
#함수 2(2)는 함수1(12)로 리턴된다
#함수1(12)는 함수0(14)로 리턴된다
#함수0(14)는 28로 리턴되기 때문에 다음과 같은 값이 나온다.
#28