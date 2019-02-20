class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1] * (n + 1)
        return self.breakhelper(n, memo)

    def breakhelper(self, n, memo):
        if n == 1:
            return 1

        memo[1] = 1

        if memo[n] != -1:
            return memo[n]
        res = -1
        for i in range(1, n):
            res = max(i * (n - i), i * self.breakhelper(n - i, memo), res)
        memo[n] = res
        return res