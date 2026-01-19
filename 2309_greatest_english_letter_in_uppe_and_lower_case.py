class Solution(object):
    def greatestLetter(self, s):
        letters = set(s)

        for ch in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(ch)
            lower = chr(ch + 32)

            if upper in letters and lower in letters:
                return upper

        return ""
