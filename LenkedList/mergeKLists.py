from ListNode import ListNode
'''
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
'''
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists)==0:return None
        return self.binarymergeKLists(lists,0,len(lists))

    def binarymergeKLists(self,lists,start,end):
        if start>end: return None
        length = end-start
        if length==1:
            return lists[start]
        if length == 2:
            return self.mergeLists(lists[start],lists[end-1])
        else:
            mid = length//2
            return self.mergeLists(self.binarymergeKLists(lists,start,start+mid),self.binarymergeKLists(lists,start+mid,end))

    def mergeLists(self,l1,l2):
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

if __name__ == "__main__":
    a = Solution()
    lists = []
    aa = ListNode(1)
    aa.next = ListNode(4)
    aa.next.next = ListNode(5)
    bb = ListNode(1)
    bb.next = ListNode(3)
    bb.next.next = ListNode(4)
    cc = ListNode(2)
    cc.next = ListNode(6)
    lists.append(aa)
    lists.append(bb)
    lists.append(cc)
    res = a.mergeKLists(lists)
    print(res)