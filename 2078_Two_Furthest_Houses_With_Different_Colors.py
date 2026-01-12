class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        ans1 = 0
        for i in range(n-1,-1,-1):
            if colors[i] != colors[0]:
                ans1 = i
                break
        ans2 = 0
        for i in range(n):
            if colors[i] != colors[n-1]:
                ans2 = (n-1) - i
                break
        return max(ans1,ans2)