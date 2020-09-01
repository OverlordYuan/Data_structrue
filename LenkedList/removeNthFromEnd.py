from ListNode import ListNode
'''
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newhead.next = head
        fast = head
        slow = newhead
        while(n>0):
            fast = fast.next
            n -= 1
        while(fast!=None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return newhead.next