class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = set()
        for num in A:
            if num in nums:
                return num
            nums.add(num)