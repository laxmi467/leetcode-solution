class Solution(object):
    def longestPalindrome(self, s):
        longest = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word == word[::-1] and len(word) > len(longest):
                    longest = word

        return longest

