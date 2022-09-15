# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number1 = l1.val
        number2 = l2.val
        
        digit = 1
        while l1.next is not None or l2.next is not None:
            if l1.next is not None:
                l1 = l1.next
                number1 += l1.val * 10 ** digit
                
            if l2.next is not None:
                l2 = l2.next
                number2 += l2.val * 10 ** digit
            
            digit += 1
            
        total = str(number1 + number2)
        
        print(total)
        
        listNode = None
        nextNode = None
        
        for index in range(len(total)):
            nextNode = ListNode(total[index])
            if listNode is not None:
                 nextNode = ListNode(total[index], listNode)
            listNode = nextNode
               
                
            
        return nextNode