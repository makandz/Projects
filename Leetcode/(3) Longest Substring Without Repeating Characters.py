# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for c_i in range(len(s)):
            c = s[c_i]
            chars = {c: 1}
            length = 1
            for i in s[c_i + 1:]:
                if i in chars:
                    break
                else:
                    length += 1
                    chars[i] = 1
            longest = max(longest, length)

        return longest