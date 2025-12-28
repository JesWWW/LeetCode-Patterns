# Binary Search 完全指南

> 透過 invariant 思維掌握二分搜尋的本質

---

## 什麼是 Binary Search？

**Binary Search** 是一種在有序或具單調性的空間中，每次比較都能排除一半候選區間的高效演算法。

### 核心價值

> **每一次比較，都必須能保證排除一半搜尋空間**

不是猜測哪邊有答案，而是證明哪邊一定沒有答案。

---

## 何時使用？

### 適用場景

| 關鍵特徵 | 範例題型 |
|---------|---------|
| sorted / non-decreasing | 標準 Binary Search |
| rotated sorted（至少一半有序） | Search in Rotated Sorted Array |
| 單調性（可判斷的條件） | Find Peak Element |
| first / last（邊界） | Search Insert Position |
| minimum / maximum（收斂性） | Find Minimum in Rotated Array |

### 判斷口訣

1. 搜尋空間有序嗎？
2. 能排除一半嗎？
3. 需要全掃嗎？（如果是，就不適用）

---

## KEY

### Invariant

```
如果答案存在，它只可能在當前區間 [L, R] 內
```

每次更新 L 或 R 時，必須確保這個 invariant 仍成立。

### Pointer 的職責

| Pointer | 意義 | 更新規則 |
|---------|------|---------|
| L | 可能包含答案的左邊界 | `L = mid + 1` |
| R | 可能包含答案的右邊界 | `R = mid - 1` 或 `R = mid` |
| mid | 用來切分的比較點 | `mid = (L + R) // 2` |

### While 條件

| 搜尋目標 | While 條件 |
|---------|-----------|
| 找具體 index | `L <= R` |
| 找邊界 / 最小最大 | `L < R` |

---

## 思考流程

每次都問這四個問題：

```
1. 搜尋空間是什麼？（index / value / answer）
2. mid 代表什麼？（nums[mid] / 判斷點）
3. 哪一半一定不可能？（核心！必須有清晰邏輯）
4. 更新後 invariant 還成立嗎？
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

**關鍵**：`while L <= R`、`L = mid + 1`、`R = mid - 1`

**適用**：Binary Search, Search Insert Position

---

### 模板 2：Lower Bound（找第一個 >= target）

```python
def lower_bound(nums, target):
    L, R = 0, len(nums)

    while L < R:
        mid = (L + R) // 2
        if nums[mid] < target:
            L = mid + 1
        else:
            R = mid  # 保留 mid，可能是答案

    return L
```

**關鍵**：`while L < R`、`R = mid`（不減 1）

**適用**：Search Insert Position, First Bad Version

---

### 模板 3：Rotated Sorted Array

**核心觀察**：[L, mid] 或 [mid, R] 其中一半一定完全 sorted

```python
def search_rotated(nums, target):
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R) // 2
        if nums[mid] == target:
            return mid

        # 判斷哪一半是 sorted
        if nums[L] <= nums[mid]:  # 左半 sorted
            if nums[L] <= target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
        else:  # 右半 sorted
            if nums[mid] < target <= nums[R]:
                L = mid + 1
            else:
                R = mid - 1
    return -1
```

**關鍵**：先判斷哪一半 sorted，再判斷 target 在不在範圍內

**適用**：Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array

---

## 練習題單

### Problems

| # | 題目 | 難度 | 類型 |
|---|------|------|------|
| 1 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | 邊界 |
| 2 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Rotated |
| 3 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | 收斂 |
| 4 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | 單調性 |
| 5 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Answer Space |

### Extras

| # | 題目 | 難度 | 類型 |
|---|------|------|------|
| 1 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | 基礎 |
| 2 | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Hard | Rotated + 重複 |

---

## Complexity

| 情況 | 時間 | 空間 |
|------|------|------|
| Binary Search | O(log n) | O(1) |
| Rotated Array | O(log n) | O(1) |

---

## 面試技巧

### 說出你的思考過程

1. "這個 array 是 sorted 的，可以用 Binary Search"
2. "我的 invariant 是：答案一定在 [L, R] 內"
3. "比較 mid 後，我可以排除左半/右半，因為..."
4. "時間複雜度是 O(log n)"

### 常見錯誤

- Integer overflow：用 `mid = L + (R - L) // 2`
- 無限迴圈：`R = mid` 時必須用 `L < R`
- 邊界處理：仔細選擇 `L <= R` vs `L < R`

---