'''
148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
通过次数87,232提交次数130,494
'''
class Solution(object):
    def sortList(self, head):
        self.quicksort(head,None)
        return head

    def quicksort(self,start,end):
        if start == None or start.next == None or start==end:return
        flag = start.val
        left = start
        right = start.next
        while(right!=end):
            if(right.val<flag):
                temp = left.next.val
                left.next.val = right.val
                right.val = temp
                left = left.next
            right = right.next
        start.val = left.val
        left.val  = flag
        self.quicksort(start,left)
        self.quicksort(left.next,right)