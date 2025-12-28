class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best, L = float(inf), 0
        total = 0
        n = len(nums)

        for R in range(n):
            total += nums[R]
            while total >= target:
                best = min(best, R-L+1)
                total -= nums[L]
                L += 1
        
        return best if best != float(inf) else 0

        