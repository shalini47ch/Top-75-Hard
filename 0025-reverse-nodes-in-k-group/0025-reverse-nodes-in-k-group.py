# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #first move till the kth node and then do the reverse logic
        count=0
        temp=head
        while(temp!=None and count<k):
            temp=temp.next
            count+=1
        if(count<k):
            return head
        prevNode=self.reverseKGroup(temp,k)
        count=0
        curr=head
        #now apply the logic of reverse
        while(count<k):
            nxt=curr.next
            curr.next=prevNode
            prevNode=curr
            curr=nxt
            count+=1
        return prevNode

       