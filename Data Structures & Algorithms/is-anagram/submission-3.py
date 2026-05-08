class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_t = "".join(sorted(t))
        sorted_s = "".join(sorted(s))
        return sorted_t == sorted_s