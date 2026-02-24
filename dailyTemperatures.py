class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waitingDays = []
        returnList = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while waitingDays and temperatures[waitingDays[-1]] < temperature:
                prev_i = waitingDays.pop()
                returnList[prev_i] = i - prev_i

            waitingDays.append(i)

        return returnList