'''
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
 示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length1 = len(nums1)
        length2 = len(nums2)
        total = length1 + length2
        left = (total+1)//2
        right = (total+2)//2
        return (self.findK(nums1,nums2,left)+self.findk(nums1,nums2,right))/2.0

    def findk(self,nums1,nums2,k):
        if len(nums1)==0:return nums2[k-1]
        if len(nums2)==0:return nums1[k-1]
        if k==1:return min(nums1[0],nums2[0])

        if len(nums1)<k//2: left1 = nums2[-1]+1
        else:left1 = nums1[k//2-1]
        if len(nums2)<k//2: left2 = nums1[-1]+1
        else:left2 = nums2[k//2-1]

        if left1<left2:
            return self.findk(nums1[k//2:],nums2,k-k//2)
        else:
            return self.findk(nums1,nums2[k//2:],k-k//2)