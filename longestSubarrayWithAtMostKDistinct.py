class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostKDistinctList(nums, k) - self.atMostKDistinctList(nums, k - 1)


    def atMostKDistinctList(self, nums: List[int], k:int) -> int:
        window = {}
        left = 0
        count = 0
        for i,n in enumerate(nums):
            window[n] = window.get(n, 0) + 1

            while(len(window) > k):
                numberOnLeftSide = nums[left]
                window[numberOnLeftSide] -= 1
                if (window[numberOnLeftSide] == 0):
                    del window[numberOnLeftSide]
                left += 1

            count += i - left + 1
        return count


