# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        dummyNode = ListNode(0)
        dummyNode.next = head
        
        cur = head
        
        while cur and cur.next:
            
            if cur.val > cur.next.val:
                placeToInsert = cur.next
                
                # Start from the beginning
                placeToInsertBefore = dummyNode
                while placeToInsertBefore.next.val < placeToInsert.val:
                    placeToInsertBefore = placeToInsertBefore.next
                
                cur.next = placeToInsert.next
                
                # Insert placeToInsert between placeToInsertBefore and placeToInsertBefore.next
                placeToInsert.next = placeToInsertBefore.next
                placeToInsertBefore.next = placeToInsert
                
            else:
                cur = cur.next
        
        return dummyNode.next
