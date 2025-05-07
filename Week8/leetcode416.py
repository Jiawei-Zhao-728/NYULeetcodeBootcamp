class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # base case: 0 sum is always possible

        for num in nums:
            for i in range(target, num - 1, -1):  # reverse to prevent reuse
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
