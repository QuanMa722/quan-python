class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        result = ''

        for i in range(len(s)):

            left1, right1 = self.expand_around_center(s, i, i)
            left2, right2 = self.expand_around_center(s, i, i + 1)

            if right1 - left1 + 1 > max_len:
                max_len = right1 - left1 + 1
                result = s[left1:right1 + 1]
            if right2 - left2 + 1 > max_len:
                max_len = right2 - left2 + 1
                result = s[left2:right2 + 1]

        return result

    @staticmethod
    def expand_around_center(s: str, left: int, right: int) -> (int, int):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
