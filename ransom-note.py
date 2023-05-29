class Solution:
    # O(M+N)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterDict = {}
        for ch in magazine:
            if ch in letterDict:
                letterDict[ch] += 1
            else:
                letterDict[ch] = 1
        for ch in ransomNote:
            if ch in letterDict and letterDict[ch] > 0:
                letterDict[ch] -= 1
            else:
                return False
        return True

    def canContruct2(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch in magazine:
                magazine = magazine.replace(ch,'',1)
            else:
                return False
        return True
