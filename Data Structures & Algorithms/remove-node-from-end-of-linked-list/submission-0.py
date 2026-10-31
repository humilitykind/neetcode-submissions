class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Advance fast pointer by n + 1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Unlink the target node
        slow.next = slow.next.next

        return dummy.next

        
            

        