import random
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rnode = ListNode(0)
        cur_node = rnode
        carry = 0
        num = 0

        while True :
            num = 0
            if l1 != None:
                num += l1.val
                l1 = l1.next
            if l2 != None:
                num += l2.val
                l2 = l2.next

            num += carry
            carry = num // 10
            num = num % 10
            cur_node.val = num

            if l1 == None and l2 == None and carry == 0:
                cur_node.next = None
                break
            new_node = ListNode(0)
            cur_node.next = new_node
            cur_node = cur_node.next
        return rnode
            

# debug
l1 = ListNode(0)
cur_node = l1
count = random.randint(5,10)
i = 0
print('prepare l1, count : ', count)
while True:
    cur_node.val = random.randint(0,9)
    i+=1
    if i == count:
        cur_node.next = None
        break
    new_node = ListNode(0)
    cur_node.next = new_node
    cur_node = cur_node.next


l2 = ListNode(0)
cur_node = l2
count = random.randint(5,10)
i = 0
print('prepare l2, count : ', count)
while True:
    cur_node.val = random.randint(0,9)
    i+=1
    if i == count:
        cur_node.next = None
        break
    new_node = ListNode(0)
    cur_node.next = new_node
    cur_node = cur_node.next

tmp = l1
while tmp != None:
    print(tmp.val,' -> ', end="")
    tmp = tmp.next
print('None')

tmp = l2
while tmp != None:
    print(tmp.val,' -> ', end="")
    tmp = tmp.next
print('None')

s = Solution()
answer = s.addTwoNumbers(l1,l2)
tmp = answer
print('Answer : ')
while tmp != None:
    print(tmp.val,' -> ', end="")
    tmp = tmp.next
print('None')




        
