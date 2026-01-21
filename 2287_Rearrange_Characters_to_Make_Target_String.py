class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        count_s = Counter(s)      
        count_t = Counter(target)
        ans = float('inf')
        for ch in count_t:
            ans = min(ans , count_s[ch] // count_t[ch])
        return ans