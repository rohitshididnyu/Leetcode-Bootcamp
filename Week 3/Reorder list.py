class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast =head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
        newhead =slow.next
        prev = slow.next = None
        while newhead:
            upnext = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = upnext
        #now merge
        l1 = head
        l2 = prev

        while l1 and l2: 
            upnext1 = l1.next
            upnext2 = l2.next
            l1.next = l2
            if not upnext1:
                break
            l2.next = upnext1
            l1 = upnext1
            l2 = upnext2
        return head
        