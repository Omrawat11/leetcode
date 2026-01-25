class Solution(object):
    def largestGoodInteger(self, num):
        max_digit = ""

        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i] > max_digit:
                    max_digit = num[i]

        if max_digit == "":
            return ""
        return max_digit * 3
