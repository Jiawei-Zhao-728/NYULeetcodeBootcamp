class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high: 
            if nums[mid] == 0:
                # Swap to move 0 towards the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 2: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

            else:
                mid += 1

