'''
215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        k = len(nums)-k
        return self.findk(nums,k)
    def findk(self,nums,k):
        left = 0
        right = len(nums)-1
        flag = nums[0]
        pos = 0
        while(left<right):
            while(left<right and nums[right]>flag):
                right -= 1
            nums[pos] = nums[right]
            pos = right
            while(left<right and nums[left]<=flag):
                left += 1
            nums[pos] = nums[left]
            pos = left
        nums[pos] = flag
        if pos==k:return flag
        elif pos>k:return self.findk(nums[0:pos],k)
        else:return self.findk(nums[pos+1:],k-pos-1)

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    a = Solution()
    res = a.findKthLargest(nums,k)
