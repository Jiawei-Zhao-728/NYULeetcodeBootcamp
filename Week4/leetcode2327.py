class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        # dp[i]: 第 i 天有多少人新知道这个秘密
        dp = [0] * (n + 1)
        dp[1] = 1  # 第一天有一个人知道

        for day in range(1, n + 1):
            sharer = dp[day] % MOD
            if sharer == 0:
                continue

            # 这个人会从 day + delay 开始，到 day + forget - 1 这段时间内每天分享一次
            for share_day in range(day + delay, min(day + forget, n + 1)):
                dp[share_day] = (dp[share_day] + sharer) % MOD

        # 统计还记得秘密的人（在还没到 forget 的日子里）
        result = 0
        for day in range(n - forget + 1, n + 1):
            result = (result + dp[day]) % MOD

        return result
