#https://velog.io/@happysang/%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A1%B0%EC%9E%91

def palindrome(text: str) -> bool:
    str = []
    for x in text:
        if x.isalnum():
            str.append(x.lower())
    #팰린드롬 여부 판별
    while len(str) > 1:
        if str.pop(0) != str.pop():
            return False
    return True


def palindrome2(text: str) -> bool:
    #자료형 데크로 선언
    str = collections.deque()
    for x in text:
        if x.isalnum():
            str.append(x.lower())

    while len(str) > 1:
        if str.popleft() != str.pop():
            return False
    return True


import re
def palindrome3(text: str) -> bool:
    str = text.lower()
    #정규식으로 불필요한 문자 필터링
    str = re.sub('[^a-z0-9]', '', str)
    return str == str[::-1]




import re, collections
def common_word(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split() 
                    if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return max(counts, key = counts.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]
print(common_word(paragraph,banned))


dict1 = {"첫번째":0, "두번째":0, "세번째":0} #이처럼 words의 요소들을 전부 키로 넣고 그 값을
                                            #0으로 지정해도 된다. 그러나 번거롭다.
dict1["두번째"] += 2
print(dict1)

dict2 = collections.defaultdict(int)
dict2["b"] += 2
#이렇게 미리 값을 정해놓지 않아도 기본 값 0으로 해서 쉽게 조작이 가능하다.
print(dict2)


c = [4,2,5,7,1,3]
print(sorted(c))
print(c)
print(c.sort())
print(c)



list = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0],s[-1]
print(sorted(list, key=fn))
print(sorted(list, key = lambda s: (s[0],s[-1])) )


#from typing import List
def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)
    for word in strs:
        #정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))





