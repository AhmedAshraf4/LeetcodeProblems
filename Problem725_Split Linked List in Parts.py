'''
Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def delete_first_node(head):
            if head is None:
                return None
            val = head.val
            new_head = head.next
            head.next = None
            return new_head , val
        
        def add_node(head, val):
            new_node = ListNode(val)
            if head is None:
                return new_node
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            return head
        
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        
        excess = length % k
        part = length / k
        out = []
        for i in range(k):
            temp = None
            for j in range(part):
                head , val = delete_first_node(head)
                temp = add_node(temp,val)
            if excess > 0:
                head , val = delete_first_node(head)
                temp = add_node(temp,val)
                excess -= 1
            out.append(temp)
        return out      