import collections
class list_node(object):
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next

class hash_map:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(list_node)

    # 삽입
    def put(self, key, value):
        index = key % self.size

        
        #인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = list_node(key, value)
            return
        
        #인덱스에 노드가 존재하는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = list_node(key, value)

    # 조회
    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p =self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = list_node() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, prev.next

    