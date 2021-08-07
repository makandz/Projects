class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        while size != 1:
            for i in range(len(s) - size + 1):
                z = s[i:i + size]
                if z == z[::-1]:
                    return z
            size -= 1

        return s[0]

x = Solution()
print(x.longestPalindrome('babad'))
print(x.longestPalindrome('cbbd'))
print(x.longestPalindrome('a'))
print(x.longestPalindrome('ac'))