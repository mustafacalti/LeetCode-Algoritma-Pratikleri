class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictim = {}
        for i,n in enumarate(nums):
            need = target - n
            if need in dictim:
                return [dictim[need],i]
            else:
                dictim[n] = i
