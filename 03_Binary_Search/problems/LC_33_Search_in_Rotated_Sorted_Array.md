# LeetCode 33 – Search in Rotated Sorted Array

🔗 [Problem Link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

**Pattern**: Binary Search (Rotated)  
**Difficulty**: Medium  
**Time**: O(log n) | **Space**: O(1)

---

## U - Understand

**問題**: 在 rotated sorted array 找 target

**key**: 至少有一半是 sorted

**限制**: 
- 原本 sorted，rotate 一次
- 元素不重複
- 需 O(log n)

**Test Cases**:
```
[4,5,6,7,0,1,2], target=0 → 4
[4,5,6,7,0,1,2], target=3 → -1
[1], target=1 → 0
```

---

## M - Match

### 直覺想法
線性掃描 → **O(n)**

### 為什麼不夠好？
題目要求 O(log n)，而且沒利用「部分有序」特性

### 優化解法
**Binary Search (Rotated 變形)** → **O(log n)**

**key**: 
- 雖然整體不完全有序
- 但 [L, mid] 或 [mid, R] 至少一半是 sorted
- 可在 sorted 那一半安全地排除

---

## P - Plan

```
1. 判斷哪一半 sorted
   - if nums[L] <= nums[mid]: 左半 sorted
   - else: 右半 sorted

2. 在 sorted 那一半檢查 target 範圍
   - 在範圍內 → 往那邊縮
   - 不在 → 往另一邊縮
```

**Invariant**: 答案只可能在 [L, R] 內

**核心**: 先判斷哪邊 sorted，再判斷 target 在不在範圍內

---

## I - Implement

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] == target:
                return mid
            
            # 左半 sorted
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            # 右半 sorted
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        
        return -1
```

---

## R - Review

**複雜度**: 
- Time: O(log n) - 每次排除一半
- Space: O(1)

**正確性**: 每次都能正確判斷哪邊 sorted，並排除不可能的一半

---

## E - Evaluate

**Edge Cases**:
- 空陣列 ✓
- 單元素 ✓
- 沒 rotate (sorted) ✓
- target 不存在 ✓

**Debug**:
- 畫圖看哪邊是 sorted
- 用小範例手動跑一遍

**Notes**:
- 一開始想不到「至少一半是 sorted」
- 忘記要先判斷哪邊 sorted
- 範圍判斷的 < 和 <= 容易搞混

---