class Solution(object):
    def removeDigit(self, number, digit):
        for i in range(len(number)):
            if number[i] == digit:
               
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i + 1:]
        
    
        last_index = number.rfind(digit)
        return number[:last_index] + number[last_index + 1:]

        