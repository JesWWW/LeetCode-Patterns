# LeetCode 704 – Binary Search

🔗 [Problem Link](https://leetcode.com/problems/binary-search/)

**Pattern**: Binary Search (Standard)  
**Difficulty**: Easy  
**Time**: O(log n) | **Space**: O(1)

---

## U - Understand

**問題**: 在 sorted array 找 target 的 index

**限制**: 
- 陣列已排序（升序）
- 找不到回傳 -1

**Test Cases**:
```
[-1,0,3,5,9,12], target=9 → 4
[-1,0,3,5,9,12], target=2 → -1
[5], target=5 → 0
```

---

## M - Match

### 直覺想法
線性掃描，逐一比較 → **O(n)**

### 為什麼不好？
沒利用到 sorted 的特性

### 優化解法
**Binary Search** → **O(log n)**

**key**: sorted → 每次比較可排除一半

---

## P - Plan

```
1. L=0, R=n-1
2. while L <= R:
   - mid = (L+R) // 2
   - nums[mid] == target → return mid
   - nums[mid] < target → L = mid+1
   - nums[mid] > target → R = mid-1
3. return -1
```

**Invariant**: 答案只可能在 [L, R] 內

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
            elif nums[mid] < target:
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

---

## E - Evaluate

**Edge Cases**:
- 空陣列 ✓
- 單元素 ✓
- target 在最左/最右 ✓
- target 不存在 ✓

**常見錯誤**:
- while L < R (應該 L <= R)
- mid 計算 overflow (用 L + (R-L)//2)

---