class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for i in reversed(range(length)):
            for w in range(length - i):
                temp = s[(w):(w+i+1)]
                if temp == temp[::-1]:
                    return temp
