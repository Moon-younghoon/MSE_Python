class OMG : 
    def print() :
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given

#조건
#class OMG : 
    #def print() :
        #print("Oh my god")
# 문제
#>>> >>> myStock = OMG()
#>>> myStock.print()
#mystock.print()를 하면 자동으로 OMG.print(mystock)과 같은 값이 나와버림
#위 조건에서는 비어있음 즉 print 안에 argument가 존재하면 안됨
#따라서 에러가 남