list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    if i.endswith(('.c','.h')):
       print(i)
# list중 h와 c로 끝나는 확장자만 출력
# 즉 list 안에c와 h로 끝나는 것만 출력하도록 코딩
# for문을 이용해 i변수 설정,list를 대입해줌
# if문을 사용해 조건문을 만들어준다.
# 이러한 변수 i 에 endwith를  사용해 c와h로 끝나는것만 출력하도록 한다
