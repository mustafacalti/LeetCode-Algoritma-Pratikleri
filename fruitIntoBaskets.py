class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        left = 0
        maximumWindowSize = 0
        for i,fruit in enumerate(fruits):
            freq[fruit] = freq.get(fruit, 0) + 1
            while(len(freq) > 2):
                fruitOnLeftSide = fruits[left]
                freq[fruitOnLeftSide] -= 1
                if(freq[fruitOnLeftSide] == 0):
                    del freq[fruitOnLeftSide]
                left += 1
            maximumWindowSize = max(maximumWindowSize, i - left + 1)
        return maximumWindowSize



