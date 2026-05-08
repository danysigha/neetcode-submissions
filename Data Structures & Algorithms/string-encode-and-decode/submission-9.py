import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for string in strs:
            s = s + str(len(string)) + ","
        # s = s[:-1]
        s = s + "#"

        for string in strs:
            s = s + string + "#"
        s = s[:-1]

        print(s)

        return s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        szs, i = [], 0
        cur = ""
        words = []

        while i < len(s):

            while s[i] != ",":
                cur += s[i]
                i+=1
            szs.append(int(cur))
            cur = ""
            i += 1

            if s[i] == "#":
                break
                
        for sz in szs:
            i += 1
            words.append(s[i:i+sz])
            i = i+sz
        
        print(szs)
        print(words)
        return words

