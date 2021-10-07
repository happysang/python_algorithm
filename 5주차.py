#Single Linked List
class ListNode(object):
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class SList(object):
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0
    
    def append(self, value):
        if self.size == 0:
            self.head = ListNode(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = ListNode(value)
            target.next = newtail
            self.size += 1
            
    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.val, '-> ', end='')
                target = target.next
            else:
                print(target.val)
                target = target.next


l1 = SList()
l1.append(2)
l1.append(4)
l1.append(3)
l1.printlist()
l2 = SList()
l2.append(5)
l2.append(6)
l2.append(4)
l2.printlist()




#문제1_1
class Solution(object):
    
    def reverse_list(self,head):
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    def to_list(self,node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def to_reversed_linked_list(self,result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1, l2):
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))
        
        result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        return self.to_reversed_linked_list(str(result))


#문제1_2
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = head = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next


#문제2_1
class Solution(object):
    def swapPairs(self, head):
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
                      
        return head


#문제2_2
class Solution(object):
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
            
        return root.next


#문제3_1
class Solution(object):
    def oddEvenList(self, head):
            if head is None:
                return None

            odd = head
            even = head.next
            even_head = head.next

            while even and even.next:
                odd.next, even.next = odd.next.next, even.next.next
                odd, even = odd.next, even.next

            odd.next = even_head
            return head 
        