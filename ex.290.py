class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()
# class에서 부모를 가져옴
#def를 이용해 _init_함수 정의해주고 위함수에서는 부모생성을 출력해준다.
#자식class는 부모class를 상속받는다
#자식 class가 생성될때 자식생성을 print한 뒤 super()을 통해 부모클래스를 호출해 생성자를 생성
#따라서 다음값이 생성될 것이다.
#자식생성
#부모생성
