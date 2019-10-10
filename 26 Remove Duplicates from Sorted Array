class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #my solution 
        #76ms(faster than 36.89%) and 13.5MB (less than 95.31%)
        nums[:] = sorted(set(nums))
        
        #suggested solution
        #56ms(faster than 99%) and 13.6MP(less than 46.88&)
        """if len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1"""
