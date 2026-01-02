# Q- 2341 - maximum number of pairs in array
class Solution(object):
    def numberOfPairs(self, nums):
        nums = [1,2,3,2,3,2,2]
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        leftover = 0
        pairs = 0
        for j in d.values():
            leftover += j % 2  # modulus operator %
            pairs += j // 2  # floor division operator // 
        return [pairs , leftover]  