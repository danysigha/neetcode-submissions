class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for item in nums:
            if item in mySet:
                return True
            mySet.add(item)
        return False