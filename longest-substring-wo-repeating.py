class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        longest = 0
        lp = 0
        if len(s) <= 1:
            return len(s)
        for rp, ch in enumerate(s):
            if ch in tracker:
                lp = max(lp, tracker[ch] + 1)
            longest = max(longest, rp - lp + 1)
            tracker[ch] = rp

        return longest


# {
#     p:0
#     w:2
# }

# pwwp
