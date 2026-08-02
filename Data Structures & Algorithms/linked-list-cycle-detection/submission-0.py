# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Build hashmap for visited
        hashmap = {}

        curr = head
        while curr:
            # Check if we've already visited the element
            if curr in hashmap:
                return True
            
            hashmap[curr] = True
            curr = curr.next
        
        return False