class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        memo = [-1] * (N + 1)
        return self.helper(N, memo)

    def helper(self, N, memo):
        if memo[N] >= 0:
            return memo[N]
        if N == 0:
            return 0
        if N == 1:
            return 1
        if memo[N] == -1:
            memo[N] = self.helper(N - 1, memo) + self.helper(N - 2, memo)

        return memo[N]