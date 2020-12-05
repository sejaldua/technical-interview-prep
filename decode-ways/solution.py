class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, len(s) + 1): 
            
            # Check if successful single digit decode is possible.
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
                
            # Check if successful two digit decode is possible.
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
                
        return dp[len(s)]