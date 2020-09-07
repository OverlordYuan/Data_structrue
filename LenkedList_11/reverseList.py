from ListNode import ListNode
'''
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
class Solution(object):
    def reverseList(self, head):
        if head==None or head.next == None:return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead

    def _reverseList(self, head):
        if head==None or head.next == None:return head
        newhead = ListNode(0)
        newhead.next = head
        current_node = head
        next_node = head.next
        while(next_node!=None):
            current_node.next = next_node.next
            next_node.next = newhead.next
            newhead.next = next_node
            next_node = current_node.next
        return newhead.next
if __name__ == "__main__":
    a = Solution()

    aa = ListNode(1)
    aa.next = ListNode(4)
    aa.next.next = ListNode(5)
    res = a._reverseList(aa)
    print(res)