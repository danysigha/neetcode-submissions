class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tally = dict()
        result = []

        for item in nums:
            tally[item] = tally.get(item, 0) + 1
        
        for key, value in tally.items():
            result.append([value, key])

        result.sort(key=lambda pair: pair[0], reverse=True)

        return [result[i][1] for i in range(k)]