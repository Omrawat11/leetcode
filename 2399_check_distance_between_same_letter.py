class Solution(object):
    def checkDistances(self, s, distance):
        first_pos = {}

        for i, ch in enumerate(s):
            if ch not in first_pos:
                first_pos[ch] = i
            else:
                actual = i - first_pos[ch] - 1
                if actual != distance[ord(ch) - ord('a')]:
                    return False

        return True