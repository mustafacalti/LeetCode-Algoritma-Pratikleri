class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        window = {0:1}
        currentSum = 0
        subArrayNumber = 0
        for i, num in enumerate(nums):
            currentSum += num
            if(currentSum - k in window):
                subArrayNumber += window[currentSum - k]
            window[currentSum] = window.get(currentSum,0) + 1

        return subArrayNumber
