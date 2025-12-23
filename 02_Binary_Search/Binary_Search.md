# Binary Search 完全指南

> Binary Search 解題筆記

---

## 目錄

- [什麼是 Binary Search？](#什麼是-binary-search)
- [何時使用？](#何時使用)
- [核心概念](#核心概念)
- [思考流程](#思考流程)
- [常見模板](#常見模板)
- [練習題單](#練習題單)

---

## 什麼是 Binary Search？

**Binary Search（二分搜尋）** 是一種在 **有排序** 的搜尋空間中，  
每次比較都能 **排除一半不可能區間** 的演算法技巧。

核心價值只有一句話：

> **每一次比較，都必須能保證丟掉一半搜尋空間**

---


## 何時使用？

### 適用場景

| 關鍵字   |  說明 |
|---------------|------|
| sorted / non-decreasing | 標準 Binary Search |
| rotated sorted | 至少一半仍有序 |
| first / last | 邊界具單調性 |
| minimum / maximum | 條件可收斂 |



### ❌ 不適用場景

- 沒有排序
- 每次比較無法排除一半
- 需要遍歷所有元素（那是 linear scan）


---

## 核心概念

### 1) Invariant

```text
Invariant:
target 只可能存在於「目前區間」[L, R]
```

### 2) Role of pointer

| 指標 | 含義 |
|------|------|
| L | 可能包含答案的左界 |
| R | 可能包含答案的右界 |
| mid | 用來切半、排除搜尋空間的比較點 |

### 3) while 條件

| 搜尋目標 | while 條件 |
|----------|------------|
| 找 index | `L <= R` |
| 找邊界 | `L < R` |
| 找最小 / 最大 | `L < R` |

---

## 思考流程


```text
1. 搜尋空間是什麼？
   - index / value / answer

2. mid 代表什麼？
   - nums[mid] 或某個條件判斷點

3. 哪一半一定不可能？
   - 可以「保證」排除的那一半直接丟掉

4. 更新 L / R 後 invariant 是否還成立？
   - target 仍只可能落在 [L, R]
```

---

## 常見模板

### 模板 1：標準 Binary Search（找 index）

```python
def binary_search(nums, target):
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

**適用題目**
- Binary Search
- Search Insert Position

---

### 模板 2：Lower Bound（找第一個 >= target）

```python
def lower_bound(nums, target):
    L, R = 0, len(nums)  # R 是開區間

    while L < R:
        mid = (L + R) // 2
        if nums[mid] < target:
            L = mid + 1
        else:
            R = mid

    return L
```

**適用題目**
- Search Insert Position


---

### 模板 3：Rotated Sorted Array

### key observations

```text
在任意狀態下：
[L, mid] 或 [mid, R] 其中一半一定是「完全sorted array」
```

```python
def search(nums, target):
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] == target:
            return mid

        # 左半sorted
        if nums[L] <= nums[mid]:
            if nums[L] <= target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1

        # 右半sorted
        else:
            if nums[mid] < target <= nums[R]:
                L = mid + 1
            else:
                R = mid - 1

    return -1
```
**適用題目**
- Search in Rotated Sorted Array
- Search in Rotated Sorted Array II


---



## 練習題單

### Easy

| # | 題目 | 難度 | 類型 | 連結 |
|---|------|------|------|------|
| 1 | Binary Search | 基礎 | [LeetCode 704](https://leetcode.com/problems/binary-search/)|
| 2 | Search Insert Position | 邊界 | [LeetCode 35](https://leetcode.com/problems/search-insert-position/) |

### Medium

| # | 題目 | 難度 | 類型 | 連結 |
|---|------|------|------|------|
| 3 | Search in Rotated Sorted Array | Medium |  旋轉 | [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| 4 | Find Minimum in Rotated Sorted Array | Medium |  收斂最小值 | [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |
| 5 | Find Peak Element | Medium |  單調性 | [LeetCode 162](https://leetcode.com/problems/find-peak-element/) |

### Hard

| # | 題目 | 難度 | 類型 | 連結 |
|---|------|------|------|------|
| 6 | Median of Two Sorted Arrays | Hard |  搜尋空間 | [LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) |
| 7 | Search in Rotated Sorted Array II | Hard |  旋轉+重複 | [LeetCode 81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) |

---

## 🎯 時間/空間複雜度

| 情況 | 時間複雜度 | 空間複雜度 |
|------|-----------|-----------|
| Binary Search | O(log n) | O(1)
| Lower Bound | O(log n) | O(1)
| Rotated Array | O(log n) | O(1)


---


