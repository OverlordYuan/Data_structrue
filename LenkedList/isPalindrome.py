from ListNode import ListNode
'''
234. 回文链表
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
class Solution(object):
    def isPalindrome(self, head):
        if head==None or head.next==None:return True
        fast = head
        slow = head
        while(fast.next!=None and fast.next.next!=None):
            fast = fast.next.next
            slow = slow.next
        slow = self.reverse(slow.next)
        fast = head
        while(slow!=None):
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse(self,head):
        if head==None or head.next==None:return head
        newhead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newhead