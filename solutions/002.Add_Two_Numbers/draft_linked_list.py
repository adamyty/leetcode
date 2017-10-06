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
        input1 = l1
        input2 = l2
        i = 0

        while True :
            num = 0
            #print('a num', num, 'carry', carry)
            if input1 != None:
                #print('input1 is not None : ', input1.val)
                num += input1.val
                input1 = input1.next
            if input2 != None:
                #print('input2 is not None : ', input2.val)
                num += input2.val
                input2 = input2.next

            num += carry
            carry = num // 10
            num = num % 10
            #print('b num', num, 'carry', carry)
            cur_node.val = num
            #print('node ', i, ' num : ', num)
            i+=1
            if input1 == None and input2 == None and carry == 0:
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
    #print('i : %d val : %d'%(i,cur_node.val))
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
    #print('i : %d val : %d'%(i,cur_node.val))
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
tmp1 = answer
while tmp1 != None:
    print(tmp1.val,' -> ', end="")
    tmp1 = tmp1.next
print('None')




        
