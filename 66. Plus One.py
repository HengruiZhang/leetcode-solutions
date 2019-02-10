class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        val = 0
        multipler = 10**(len(digits)-1)
        for i in digits:
            val = i*multipler+val
            multipler = multipler / 10
        add_one_val = val + 1
        res = list(map(int, str(add_one_val)) )
        return res