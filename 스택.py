from typing import AnyStr, List


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())


#문제1
def isValid(s: str):
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


def q1(temperatures,num,res):
    count = 0
    for x in range(len(temperatures)):
        if temperatures[0] >= temperatures[x]:
            if x == len(temperatures)-1:
                res.append(0)
                temperatures.pop(0)
                q1(temperatures, num+1, res)   
            count += 1
        else:
            res.append(count)
            temperatures.pop(0)
            q1(temperatures, num+1, res)
            
        if len(temperatures) == 0:
            return res
# print(q1([73,74,75,71,69,72,76,73], 0, []))


def q2(temperatures, res):
    for x in range(len(temperatures)):
        count = 0
        for y in range(x, len(temperatures)):
            if temperatures[x] >= temperatures[y]:
                count += 1
                if y == len(temperatures)-1:
                    res.append(0)
                continue
            else:
                res.append(count)
                break
    return res
# print(q2([73,74,75,71,69,72,76,73], []))


def dailyTemperature(temperatures:List[int]):
    answer = [0]*len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        #현재 온도가 스택 값보다 높다면 정답처리
        print(answer, stack)
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer

print(dailyTemperature([73,74,75,71,69,72,76,73]))

def removeDuplicateLetters1(s: str):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        print(suffix)
        if set(s) == set(suffix):
            return char + removeDuplicateLetters1(suffix.replace(char,''))
    return ''
# print(removeDuplicateLetters("cbacdcbc"))

import collections
def removeDuplicateLetters2(s: str):
    counter, stack = collections.Counter(s), []
    
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
            
        #뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)
        
    return ''.join(stack)
print(removeDuplicateLetters2("cbacdcbc"))


import collections
class Mystack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        #요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0