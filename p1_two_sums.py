class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            if target - nums[i] in nums and i != nums.index(target - nums[i]):
                k =  [i, nums.index(target - nums[i])]
                #print(k)
                return sorted(k)
        
        '''
        
        This soln assumes that the list passed it sorted
        
        if len(nums) <= 1:
            return []
        s = 0
        l = len(nums) - 1
        while True:
            add = nums[s] + nums[l]
            if add < target:
                s += 1
            elif add > target:
                l -=1
            else:
                return [s, l]
        '''
        