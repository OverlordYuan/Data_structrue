'''
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''
class Solution(object):
    def searchRange(self, nums, target):
        if len(nums)==0:return [-1,-1]
        left = self.left_bound(nums,target)
        right = self.right_bound(nums,target)
        return [left,right]

    def left_bound(self,nums,target):
        if len(nums)==0:return -1
        left = 0
        right = len(nums)
        while(left<right):
            mid = (left+right)//2
            if nums[mid] < target:
                left =mid+1
            else:
                right = mid
        if left==len(nums) or nums[left]!=target:return -1
        else:return left

    def right_bound(self,nums,target):
        if len(nums)==0:return -1
        left = 0
        right = len(nums)
        while(left<right):
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if left==0 or nums[left-1]!=target:return -1
        else:return left-1
