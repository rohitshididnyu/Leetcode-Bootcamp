class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod= 10**9+ 7 
        dp = [0] * (n+1) 
        dp[1] = 1
        for day in range(1,n+1):
            for share_day in range(day+delay, min(n,day+forget -1)+1):
                dp[share_day] = (dp[share_day] + dp[day]) % mod 
        
        total = 0 
        for day in range(n-forget+1, n+1):
            if day >=1:
                total = (total + dp[day]) % mod
        return total
        