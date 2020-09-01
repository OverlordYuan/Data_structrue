from ListNode import ListNode
'''
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        sum = l1.val + l2.val
        res = l1
        l1.val = sum%10
        flag = sum//10
        while(l1.next!=None and l2.next!=None):
            l1 = l1.next
            l2 = l2.next
            sum = l1.val + l2.val + flag
            l1.val = sum%10
            flag = sum//10
        if l1.next!=None or l2.next!=None:
            if l2.next!=None:
                l1.next = l2.next
            while(l1.next!=None and flag!=0):
                l1 = l1.next
                sum = l1.val +flag
                l1.val = sum%10
                flag = sum//10
        if flag!= 0:
            l1.next = ListNode(flag)
        return res