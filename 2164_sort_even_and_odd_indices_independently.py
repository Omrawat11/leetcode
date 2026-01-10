class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = sorted(nums[::2])
        odd = sorted(nums[1::2],reverse = True)
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e]
                e +=1
            else:
                nums[i] = odd[o]
                o +=1
        return nums