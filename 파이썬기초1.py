#https://velog.io/@happysang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
#https://velog.io/@happysang/1.-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 인덴트
# 탭하나에 공백 4칸. 강제는 아니고 선택적으로 적용이 가능하다.
def long_function_name(var_one, var_two, var_three, var_four):
    pass

# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)

# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)


#네이밍 컨벤션
camelCase : int = 1
snake_case : int = 1


#타입힌트
#이와 같이 작성하면 a가 정수형임을 분명하게 알 수 있으며 리턴 값으로 
# True 또는 False를 리턴할 것이라는 점도 확실하게 알 수 있다. 
# 가독성이 좋아지고 버그 발생 확률도 줄일 수 있다.
# 물론 실제로는 강제 규약이 아니다보니 동적으로 할당될 수 있으므로 주의가 필요하다.
num = 1
num : int = 1
name = "khs"
name : str = "khs"

def fn(a:int) -> bool:
    if a > 10 : return True
    else : return False


#리스트 컴프리헨션 하기 전에~


# 파이썬 람다식 lambda 인자 : 표현식
def sum(x, y):
    return x + y

print(sum(10,20))
print((lambda x,y : x + y)(10,20))


# map map(함수, 리스트) 
# 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아준다.
def squared(list,res):
    for i in range(len(list)):
        res.append(list[i]**2)
    return res

print(squared([1,2,3,4,5],[]))
print(list(map(lambda x : x**2, [1,2,3,4,5])))
print(list(map(lambda x : x**2, range(1,6) )))


#reduce() reduce(함수, 시퀀스)
from functools import reduce

print (reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))

str = "abcde"
print ( reduce(lambda x,y : y + x, str) )
print(''.join(reversed(str))) # reverse는 list에만 사용 가능


#filter()  
# filter(함수, 리스트) 리스트 원소들을 함수에 적용하여 결과가 True인 값만 뽑아서 새로운 리스트를 만든다.
print( list(filter(lambda x: x < 5, range(10))) )


#리스트 컴프리헨션
print( [x for x in range(10)] )
print( [x**2 for x in [1,2,3,4,5]] ) ## print(list(map(lambda x : x**2, [1,2,3,4,5])))
print( [x for x in range(10) if x < 5] ) ##filter


# 파이썬은 람다식의 구문도 지원을 하는데요.
# 이처럼 한줄로 간결하게 작성할 수 있는 리스트 컴프리헨셩는 가독성이 좋은 편이지만 
# 너무 무리하게 복잡하게 작성할 경우 가독성을 떨어뜨릴 수 있으므로 적절히 사용하는 게 중요하다. 
# 대체로 표현식은 2개를 넘지 않아야한다.

#제너레이터
# 예를 들어 임의의 조건으로 숫자 1억 개를 만들어내 계산하는 프로그램을 작성한다고 가정해보자. 
# 이 경우 제너레이터가 없다면 메모리 어딘가에 만들어낸 숫자 1억개를 보관하고 있어야 한다. 
# 그러나 제너레이터를 이용하면, 단순히 제너레이터만 생성해두고 필요할 때 언제든 순자를 만들어낼 수 있다. 
def yield_p():
    n = 0
    while True:
        n+=1
        yield n

g = yield_p()
for _ in range(0,50):
    print(next(g))


#range
a = [n for n in range(100000)]
b = range(100000)

if len(a) == len(b):
    print("true")

#그러나 a에는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재한다.
# print(a)
# print(b)

import sys
print(sys.getsizeof(a))
print(sys.getsizeof(b))

# 둘 사이의 메모리 점유율을 비교해보면 range 클래스를 리턴하는 방식의 장점이 쉽게 와닿을 것이다.
# 똑같이 숫자 100만개를 갖고 있으나 range클래스를 이용하는 b변수의 메모리 점유율이 훨씬 더 작다. 
# 100만개가 아니라 1억개라도 b번수의 메모리 점유율은 동일하다. 
# 생성 조건만 보관하고 있기 때문이다. 
# 게다가 미리 생성하지 않은 값은 인덱스에 접근이 안될 거라 생각할 수 있으나 
# 인덱스로 접근 시에는 바로 생성하도록 구현되어 있기 때문에 불편함없이 사용할 수 있다.

#enumerate
a = [23,45,12,52,17,63]
print(list(enumerate(a)))

for i,v in enumerate(a):
    print(i,"번째 원소:",v)


#나눗셈
print(10/3)
print(10//3)
print(divmod(10,3))


#print
print('aa', end = '')
print('bb')
a = ['A', 'B']
print(','.join(a))   #' '사이에 넣은 값을 구분자로 지정한다.

idx = 1
fruit = "Apple"
print(f'{idx+10} {fruit}')


#pass
class My_class(object):
    def method_a(self):
        pass

    def method_b(self):
        print("Method B")

c = My_class()


#local
# 로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령어이므로 디버깅에 많은 도움이 된다. 
# 변수명을 일일이 차아낼 필요 없이 로컬 스코프에 정의된 모든 변수를 출력하기 때문에 편리하다.
# pprint로 출력하게 되면 보기 좋게 줄바꿈 처리를 해주기 때문에 가독성이 높다.
import pprint
pprint.pprint(locals())
print(locals())