def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
# def를 사용하여 print_max 의 함수정의, 세 숫자이기 때문에(a,b,c) 
#if 문을 사용하여 a가 가장크면 max_val로 정의된 값이 a로, b가 가장크면 b로, c가 가장크면 c로 출력되는 조건문을 프린트하는 함수를 정의 
#max_val을 출력한다면 a,b,c중 가장 큰 값이 출력될 것 이다.