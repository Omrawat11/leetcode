class Solution(object):
    def digitCount(self, num):
        count = [0] * 10

        # Count frequency of each digit
        for ch in num:
            count[int(ch)] += 1

        # Verify the condition
        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False

        return True
