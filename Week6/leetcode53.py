class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        result = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            result = max(result, current)

        return result

