class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1 += nums2
        len_nums = len(nums1)
        nums1.sort()
        if len_nums % 2 == 0:
            return (nums1[len_nums // 2 - 1] + nums1[len_nums // 2]) / 2
        else:
            return nums1[len_nums // 2]
