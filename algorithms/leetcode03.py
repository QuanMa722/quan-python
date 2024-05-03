
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        if not s:
            return 0

        char_indices = {}
        start = max_length = 0

        for i in range(len(s)):
            if s[i] in char_indices and start <= char_indices[s[i]]:
                start = char_indices[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            char_indices[s[i]] = i

        return max_length