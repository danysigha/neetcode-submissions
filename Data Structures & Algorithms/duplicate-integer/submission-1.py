class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for item in nums:
            mySet.add(item)
        return len(mySet) != len(nums)