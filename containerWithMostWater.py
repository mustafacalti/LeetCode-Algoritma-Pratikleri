class Solution:
    def maxArea(self, height: List[int]) -> int:
        bestVolume = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            lefth = height[left]
            righth = height[right]
            currentVolume = (right-left) * min(lefth,righth)
            if(currentVolume > bestVolume):
                bestVolume = currentVolume
            if(lefth > righth):
                right-=1
            else:
                left+=1

        return bestVolume
