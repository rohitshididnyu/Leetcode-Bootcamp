class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast= fast.next.next
        newhead = slow
        prev= None
        while newhead:
            upnext = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = upnext
        l1 = head
        l2 = prev
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2=l2.next
        return True