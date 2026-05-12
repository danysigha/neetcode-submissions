class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        length = 1
        maxi_len = 1

        if not len(nums):
            return 0

        for num in nums:
            mySet.add(num)
        
        for num in nums:
            if num - 1 not in mySet:
                while num + length in mySet:
                    length += 1
                if length > maxi_len:
                    maxi_len = length
                length = 1
        return maxi_len
