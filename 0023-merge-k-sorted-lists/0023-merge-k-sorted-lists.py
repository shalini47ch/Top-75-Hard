# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #we will use the concept of k way merge to solve this 
        minheap=[]
        dummy=ListNode(-1)
        curr=dummy
        for ind,node in enumerate(lists):
            if(node):
                heapq.heappush(minheap,[node.val,ind,node])
        #now keep iterating while length of the minheap is greater than 0
        while(len(minheap)>0):
            val,indi,node=heapq.heappop(minheap)
            curr.next=node
            curr=curr.next
            if(node.next!=None):
                heapq.heappush(minheap,[node.next.val,indi,node.next])
        return dummy.next
        
        


       