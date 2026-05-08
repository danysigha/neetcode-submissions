class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = dict()
        for item in strs:
            key = "".join(sorted(item))
            result = groups.get(key, [])
            result.append(item)
            groups[key] = result

        return [groups[key] for key in groups]    