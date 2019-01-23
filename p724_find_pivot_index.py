class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        #if len(nums) == 1: return 0
        running_sum = 0
        for i in range(0, len(nums)):
            if i != 0:
                running_sum = running_sum + nums[i-1]
                if s - running_sum - nums[i] == running_sum:
                    return i
            else:
                if running_sum == s - nums[0]:
                    return 0
        return -1
        