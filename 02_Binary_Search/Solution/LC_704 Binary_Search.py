class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L, R = 0, n-1
        
        while L <= R:
            mid = (L+R) // 2
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
        return -1
        