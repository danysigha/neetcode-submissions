class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()
        for i in range(len(nums)):
            
            diff = target - nums[i]
            index = diffs.get(diff, None)
            if index != None and i!= index:
                return [index, i] if i > index else [i, index]
            
            diffs[nums[i]] = i