def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
#B
#C
#B
#C
#B
#C
#A
#def를 이용해 message 1,2,3의 함수를 정의해준다.
#message1은 A를 출력하는함수, message2는 B를 출력하는함수이다.
#message3은 message2와 c를출력한다. 즉 B와C를출력한다.
#그리고 여기서 for문은 제시된 데이터만큼 출력된ㅏ. 여기서는 3까지이기 때문에 B,C가 3번출력된다.
#그 후 message1함수가 있기 때문에 A를 출력해준다.  