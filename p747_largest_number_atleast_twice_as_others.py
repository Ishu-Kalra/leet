class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = max(nums)
        i = nums.index(M)
        #print(i)
        new_nums = [j for j in nums if j!= M]
        if not new_nums: return 0
        #print(nums[:M],nums[M+1:])
        second_M = max(new_nums)
        #print(new_nums, second_M, M)
        if second_M * 2 <= M:
            return i
        return -1