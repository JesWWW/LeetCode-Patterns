class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        best = total

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            best = max(best, total)

        return best / k