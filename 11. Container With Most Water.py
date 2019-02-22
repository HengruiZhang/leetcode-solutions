class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        vol = 0
        while l < r:
            vol = max(vol, min(height[r], height[l]) * (r - l))
            print(vol)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return vol


