# LeetCode 643 – Maximum Average Subarray I

🔗 [Problem Link](https://leetcode.com/problems/maximum-average-subarray-i/)

**Pattern**: Sliding Window (Fixed Size)  
**Difficulty**: Easy  
**Time**: O(n) | **Space**: O(1)

---

## U - Understand

**問題**: 找長度 = k 的 subarray，平均值最大

**限制**: 
- 連續 subarray
- 1 ≤ k ≤ n ≤ 10⁵
- 可能有負數

**KEY**: k 固定 → 找 sum 最大的 window

**Test Cases**:
```
[1,12,-5,-6,50,3], k=4 → 12.75 (window: [12,-5,-6,50])
[-1], k=1 → -1.0
```

---

## M - Match

### 直覺想法（次優）
每個 window 都重新算 sum → **O(nk)**

```python
for i in range(n - k + 1):
    current_sum = sum(nums[i:i+k])  # 每次都算
    best = max(best, current_sum)
```

### 為什麼不夠好？
重複計算！前一個 window 和下一個 window 只差兩個元素

### 優化解法
**Sliding Window (Fixed Size)** → **O(n)**

**KEY**: 
- 下一個 window = 前一個 - 左邊 + 右邊
- 增量更新，不用重算

---

## P - Plan

```
1. 初始 window: sum(前 k 個)
2. 從 i=k 開始滑動:
   - sum += nums[i]      (加新的)
   - sum -= nums[i-k]    (減舊的)
   - 更新 best
3. return best / k
```

**Invariant**: current_sum = 當前 window [i-k+1, i] 的總和

---

## I - Implement

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        best = current_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i]
            current_sum -= nums[i - k]
            best = max(best, current_sum)
        
        return best / k
```

---

## R - Review

**Complexity**: 
- Time: O(n) - 每個元素訪問一次
- Space: O(1) - 只用常數變數

**為什麼是 O(n) 不是 O(nk)**:
- 初始化 O(k)
- 滑動 O(n-k)
- 總共 O(n)

---

## E - Evaluate

**Edge Cases**:
- k = 1 ✓
- k = n ✓
- 全負數 ✓

**Notes**:
- 一開始想不到可以增量更新
- 忘記 best 要初始化為 current_sum（不是 0）

**Common Errors**:
- 忘記除以 k
- best = 0（全負數會錯）

---