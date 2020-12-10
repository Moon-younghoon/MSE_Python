fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
question= input("좋아하는 과일은?")
if question in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
# fruit라는 딕셔너리 안에 딸기, 토마토, 사과라는 value값이 존재한다.
# 좋아하는 과일은?이라는 물음에 value 값의 대답이 아니면 "오답입니다".를 출력, value값의 대답이라면 "정답입니다."를 출력하고싶다.
# 물음이 먼저 나와야함, question으로 물음을 정의해준 후 그곳에 물음인 "좋아하는 과일은?"을 input해준다.
# if의 조건문을 사용하여fruit의 value 값이면 정답입니다를 출력,else를 이용해 아니면 오답입니다를 출력하도록 한다.
