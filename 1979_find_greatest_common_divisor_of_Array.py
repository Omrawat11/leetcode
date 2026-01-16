class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1 = min(nums)
        n2 = max(nums)
        while n2:
            n1, n2 = n2 , n1 % n2
        return n1