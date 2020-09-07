'''
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums)==0 or len(nums)==1:return len(nums)
        tail = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
            else:
                tail[self.right_bound(tail,nums[i])] = nums[i]
        return len(tail)

    def right_bound(self,nums,target):
        left = 0
        right = len(nums)
        while(left<right):
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid
        if left==len(nums):return left-1
        return left

if __name__ == '__main__':
    a = Solution()
    nums = [4,10,4,3,8,9]
    res =  a.lengthOfLIS(nums)
    print(res)


