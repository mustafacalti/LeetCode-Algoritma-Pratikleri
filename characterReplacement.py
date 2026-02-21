class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currentWindow = {}
        left = 0
        maximumWindowSize = 0
        maxFreq = 0

        for i,ch in enumerate(s):
            currentWindow[ch] = currentWindow.get(ch,0) + 1
            maxFreq = max(maxFreq, currentWindow[ch])
            while (i-left+1) - maxFreq > k:
                leftChar = s[left]
                currentWindow[leftChar] -= 1
                left += 1

            maximumWindowSize = max(maximumWindowSize, i - left + 1)

        return maximumWindowSize







