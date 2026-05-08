class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        copy = nums[:]
        for i in range(len(nums)):
            cur_product = 1
            copy.pop(i)
            for j in range(len(copy)):
                cur_product *= copy[j]
            result.append(cur_product)
            copy = nums[:]
        return result