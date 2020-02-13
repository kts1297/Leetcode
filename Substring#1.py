# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        dummy = []
        x = 0
        while x < len(s):
            if s[x] not in dummy:
                dummy.append(s[x])
                if max_len < len(dummy):
                    max_len = len(dummy)
                x += 1
            else:
                dummy.pop(0)
        return max_len