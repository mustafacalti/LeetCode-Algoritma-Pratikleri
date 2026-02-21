class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        bestIndexs = []
        left = 0
        longestLength = 0
        for i,c in enumerate(s):
            while(c in seen):
                seen.remove(s[left])
                left = left + 1
            seen.add(c)
            currentSubsLength = i - left + 1
            if currentSubsLength > longestLength:
                longestLength = currentSubsLength
                bestIndexs = [left,i]

        return longestLength

ALTERNATIF


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        longestLength = 0

        for i, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1

            seen[c] = i
            longestLength = max(longestLength, i - left + 1)

        return longestLength










