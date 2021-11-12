def fac(num):
    res = 1
    for x in range(num,1,-1):
        res *= x
    return res
print(fac(int(input())))


def ex1(n):
    if n == 1:
        return "끝 "
    else:
        return ex1(n-1) + "재귀 "
print(ex1(5))


num = int(input())
res = []
def ex2(n):    
    if n==1:
        res.append(1)
        return res
    else:
        print(n)
        if num % n == 0:
            res.append(n)
        return ex2(n-1)
print(ex2(num))


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)
print(fac(int(input())))


def fi(n):
    nums = [0,1]
    if n == 0 or n == 1:
        return n
    else:   
        for x in range(n-1):
            nums.append(nums[0] + nums[1])
            nums.remove(nums[0])
    return nums[-1]
print(fi(10))

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(int(input())))



def star(n): 
    if n == 1: 
        return ['*']
    stars = star(n//3) 
    res = [] 
    for x in stars:
        res.append(x*3) 
    for x in stars: 
        res.append(x+' '*(n//3)+x) 
    for x in stars: 
        res.append(x*3)
    return res
n = int(input()) 
print('\n'.join(star(n)))