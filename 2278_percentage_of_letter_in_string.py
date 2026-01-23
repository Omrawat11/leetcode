class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0
        
        for ch in s:
            if ch == letter:
                count += 1
        
        percentage = (count * 100) // len(s)
        return percentage 