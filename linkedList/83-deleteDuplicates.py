# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # está em ordem crescente, então uma duplicata está sempre no proximo nó

        prev = ListNode(None, head)
        curr = head

        while curr:
            
            if prev.val == curr.val:
                #remove
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
            
        return head