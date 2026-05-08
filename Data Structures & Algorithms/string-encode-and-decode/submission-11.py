class Solution:

    def encode(self, strs: List[str]) -> str:
        szs, s = [], ""

        if not len(strs):
            return s

        for string in strs:
            s += (str(len(string)) + ",")
        s += "#"

        for string in strs:
            s += string

        # print(s)
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
        
        i += 1
        for sz in szs:
            words.append(s[i:i+sz])
            i = i+sz
        
        # print(szs)
        # print(words)
        return words
