from ListNode import ListNode
'''
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:return l2
        if l2 == None:return l1
        if l2.val<l1.val:
            temp = l1
            l1 = l2
            l2 = temp
        res = l1
        next = l1.next
        while next!=None and l2!=None:
            if l2.val<next.val:
                l1.next = l2
                l2 = l2.next
                l1 = l1.next
                l1.next = next
            else:
                l1 = next
                next = l1.next
        if l2!=None:
            l1.next = l2
        return res