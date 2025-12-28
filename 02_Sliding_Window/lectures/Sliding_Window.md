# Sliding Window 完全指南

> 透過 pointer 職責與 invariant 掌握滑動窗口

---

## 什麼是 Sliding Window？

**Sliding Window** 是處理連續 subarray/substring 問題的演算法技巧。

### 視覺化

```
nums = [1, 3, 2, 5, 1, 4, 2]
       [1 3 2]  ← window
        L   R
         [3 2 5]  → 往右滑動
          L   R
```

### 核心思想

- **Right pointer**：擴張 window（加入新元素）
- **Left pointer**：收縮 window（移除元素）
- 維護 window 內的狀態（sum、count、frequency）
- 利用前一個 window 的結果做增量更新 → O(n)

---

## 何時使用？

### 適用場景

| 關鍵字 | 範例題目 |
|--------|---------|
| subarray / substring（連續） | Minimum Size Subarray Sum |
| consecutive | Max Consecutive Ones III |
| longest / shortest | Longest Substring Without Repeating |
| at most k | Longest Substring with At Most K Distinct |
| without repeating | Longest Substring Without Repeating |

### 必須滿足

1. 要求**連續**區間
2. 可用**擴張-收縮**邏輯
3. 狀態可**增量更新**

---

## 核心概念

### Invariant

```
窗口 [L, R] 內的狀態，永遠代表一個「合法或接近合法」的解
```

### Pointer 職責（固定！）

```python
Right (R):  擴張 window
            for right in range(n)
            加入 arr[right]

Left (L):   收縮 window
            while 某條件
            移除 arr[left]
```

### 關鍵決策：while 條件

**while 條件 = 什麼時候 window 不合法？**

| 題目要求 | while 條件 |
|---------|-----------|
| 找**最短** subarray, sum **>= target** | `while total >= target` |
| 找**最長** substring, **at most k** 個 X | `while count > k` |
| 找**最長** substring, **without** repeating | `while char in seen` |

### 記憶口訣

```
"at most k"        → while xxx > k
">= target" 且找最短 → while xxx >= target
"without xxx"      → while 有 xxx
```

---

## 思考流程

### 四步驟

```
1. Window 內要統計什麼？
   → total / count / seen

2. R 擴張時做什麼？
   → total += arr[right]
   → seen.add(arr[right])

3. 什麼時候收縮 L？
   → 看題目套用 while 條件

4. L 收縮時做什麼？
   → total -= arr[left]
   → seen.remove(arr[left])
```

---

## 常見模板

### 模板 1：找最長（可變窗口）

```python
def longest_window(arr):
    left = 0
    window_state = {}  # or set()
    best = 0

    for right in range(len(arr)):
        # 1. 擴張
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1

        # 2. 不滿足 → 收縮
        while 不滿足條件(window_state):
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1

        # 3. 更新最長
        best = max(best, right - left + 1)

    return best
```

**KEY**：只在不合法時收縮

**適用**：Longest Substring Without Repeating, Max Consecutive Ones III

---

### 模板 2：找最短（可變窗口）

```python
def shortest_window(arr, target):
    left = 0
    window_state = {}
    best = float('inf')

    for right in range(len(arr)):
        # 1. 擴張
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1

        # 2. 滿足 → 持續收縮
        while 滿足條件(window_state):
            best = min(best, right - left + 1)
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1

    return 0 if best == float('inf') else best
```

**KEY**：在 while 內部更新答案（收縮前）

**適用**：Minimum Size Subarray Sum, Minimum Window Substring

---

### 模板 3：固定大小窗口

```python
def fixed_window(arr, k):
    window_state = 0
    best = float('-inf')
    
    for right in range(len(arr)):
        # 1. 加入 right
        window_state += arr[right]
        
        # 2. 窗口大小達到 k
        if right >= k - 1:
            best = max(best, window_state)
            # 移除 left
            window_state -= arr[right - k + 1]
    
    return best
```

**KEY**：`if right >= k - 1`、`right - k + 1`

**適用**：Maximum Average Subarray I, Sliding Window Maximum

---

### 模板 4：計數型（求個數）

```python
def count_window(arr):
    left = 0
    window_state = 初始值
    count = 0

    for right in range(len(arr)):
        # 1. 擴張
        window_state = 加入(arr[right])

        # 2. 不滿足 → 收縮
        while 不滿足條件(window_state):
            window_state = 移除(arr[left])
            left += 1

        # 3. 計數：以 right 結尾的合法 subarray 數量
        count += right - left + 1

    return count
```

**KEY**：每個 right 貢獻 `right - left + 1` 個 subarray

**適用**：Subarray Product Less Than K, Count Number of Nice Subarrays

---

## 練習題單

### Problems

| # | 題目 | 難度 | 類型 |
|---|------|------|------|
| 1 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | 可變窗口 |
| 2 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | HashSet |
| 3 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | HashMap 進階 |

### Extras

| # | 題目 | 難度 | 類型 |
|---|------|------|------|
| 1 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | 固定窗口 |
| 2 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | K 次容錯 |
| 3 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | HashMap (≤2) |
| 4 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | 計數進階 |
| 5 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | 固定窗口 |

---

## Complexity

| 情況 | 時間 | 空間 |
|------|------|------|
| Basic Sliding Window | O(n) | O(1) 或 O(k) |
| Use HashSet/HashMap | O(n) | O(min(n, m)) 或 O(k) |

註：雖有 while 迴圈，但 left 最多移動 n 次，總時間仍是 O(n)

---

## 面試技巧

### 說出你的思考過程

1. "這是連續 subarray 問題，可以用 Sliding Window"
2. "我的 invariant 是：window 內永遠維持合法或接近合法狀態"
3. "Right 負責擴張，Left 負責收縮"
4. "時間複雜度是 O(n)"

### 常見錯誤

- 忘記更新 window state
- while 條件寫反（最長/最短搞混）
- 答案更新時機錯誤（應在 while 內或外）
- 忘記處理 edge case（空陣列、k > n）

---