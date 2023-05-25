class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        oddCounter = 0
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                oddCounter += 1
            else:
                oddCounter -= 1
        if oddCounter > 1:
            return len(s) - oddCounter + 1
        return len(s)