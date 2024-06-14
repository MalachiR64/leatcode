# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_reverse = self.reverse_linked_list(l1)
        l2_reverse = self.reverse_linked_list(l2)
        num = self.convert(l1_reverse) + self.convert(l2_reverse)
        res = [int(x) for x in str(num)]
        head = l3 = ListNode(res.pop())
        c = res[::-1]
        for i in c:
            l3.next = ListNode(i)
            l3 = l3.next

        return head
    def reverse_linked_list(self,listNode):
        reversedlist = []
        temp = listNode
        while temp.next != None:
            reversedlist.append(temp.val)
            temp = temp.next
        reversedlist.append(temp.val)
        return reversedlist[::-1]
    
    def convert(self,r_list):
        s = [str(i) for i in r_list]
        res = int("".join(s))
        return(res)
    