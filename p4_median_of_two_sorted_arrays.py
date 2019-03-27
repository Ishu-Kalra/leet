class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0
        nums_merged = sorted(nums1 + nums2)
        if len(nums_merged) % 2 == 1:
            return nums_merged[len(nums_merged) // 2 ]
        else:
            print('Imma here', nums_merged)
            k=nums_merged[len(nums_merged) // 2]
            l=nums_merged[len(nums_merged) // 2 - 1]
            print(k,l, float(k+l)/2)
            return float(k+l)/2
        