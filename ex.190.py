apart = [ [101, 102], [201, 202], [301, 302] ]
for 층 in apart:
    for 집 in 층:
        print(집,"호")
print(-------)
# for 층 in apart 를 통해 층별로 나눔(출력한다면 [101,102]호 [201,202]호..로 나올것이다)
#이를 호 별로 또 나눠야 하기 때문에 위 상태에서 for문을 이용해 집이라는 변수를 만들어준다.
# print를 이용해 변수 집을 뽑아준다. 뒤에는"호" 붙인다.
#302호 뒤에도 계속 층이 이어지기 때문에 -------를 출력하도록 한다.
