class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        bar_count = 0
        for ch in s:
            if ch  == '|':
                bar_count +=1
            elif ch == '*' and bar_count % 2 == 0:
                count+=1
        return count