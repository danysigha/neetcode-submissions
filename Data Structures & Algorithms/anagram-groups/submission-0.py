class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for item in strs:
            found_group = False
            if len(output):
                for group in output:
                    if len(group[0]) == len(item) and sorted(item) == sorted(group[0]):
                        group.append(item)
                        found_group = True
                        break
                if not found_group:
                    output.append([item])
            else:
                output.append([item])
        return output