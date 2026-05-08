class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()
        for i in range(len(nums)):
            diffs[nums[i]] = i
        
        for j in range(len(nums)):
            diff = target - nums[j]
            index = diffs.get(diff, False)
            if index and j!= index:
                return [j, index]