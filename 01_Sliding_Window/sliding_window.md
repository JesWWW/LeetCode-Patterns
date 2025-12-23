#  Sliding Window 完全指南

> 一份完整的 Sliding Window 解題筆記，適合 LeetCode Medium 題目練習

---

## 目錄

- [什麼是 Sliding Window？](#什麼是-sliding-window)
- [何時使用？](#何時使用)
- [核心概念](#核心概念)
- [思考流程](#思考流程)
- [常見模板](#常見模板)
- [題型分類](#題型分類)
- [經典題目](#經典題目)
- [常見錯誤](#常見錯誤)
- [練習題單](#練習題單)

---

## 什麼是 Sliding Window？

**Sliding Window（滑動窗口）** 是一種用於處理 **連續子陣列/子字串** 問題的演算法技巧。

### 視覺化
```
nums = [1, 3, 2, 5, 1, 4, 2]
        ↓
       [1 3 2]  ← window (size = 3)
        L   R

往右滑動：
         [3 2 5]
          L   R

繼續滑動：
           [2 5 1]
            L   R
```

### 核心思想

- 維護一個 **可變大小或固定大小** 的窗口
- **Right 指標** 負責擴張窗口（加入新元素）
- **Left 指標** 負責收縮窗口（移除元素）
- 在過程中維護窗口內的某個狀態（總和、計數、集合等）

---

## 何時使用？

###  適用場景

當題目出現以下關鍵字時，考慮使用 Sliding Window：

| 關鍵字 | 說明 | 例題 |
|--------|------|------|
| **subarray** / **substring** | 連續的子陣列/子字串 | Minimum Size Subarray Sum |
| **consecutive** | 連續的 | Max Consecutive Ones III |
| **longest** / **shortest** | 最長/最短 | Longest Substring Without Repeating |
| **at most k** | 最多 k 個 | Longest Substring with At Most K Distinct |
| **exactly k** | 恰好 k 個（進階） | Subarrays with K Different Integers |
| **without repeating** | 不重複 | Longest Substring Without Repeating |

### ✅ 必須滿足的條件

1.  要求 **連續** 的區間（subarray/substring）
2.  可以用 **擴張-收縮** 的邏輯維護窗口
3.  窗口內的狀態可以 **增量更新**（不用每次重新計算）

### ❌ 不適用場景

- 需要跳著選元素（用 DP 或其他技巧）
- 需要找所有組合（用 Backtracking）
- 不連續的區間問題

---

## 核心概念

###  指標職責（固定的！）
```python
Right (R) 指標：
   永遠只做一件事：擴張 window
   for right in range(n) 自動往右移動
   每次加入 arr[right]

Left (L) 指標：
   永遠只做一件事：收縮 window
   while 某條件時 left += 1
   每次移除 arr[left]
```

###  關鍵決策：while 條件

**while 條件 = 「什麼時候窗口不合法，需要收縮？」**

| 題目要求 | while 條件 | 原因 |
|---------|-----------|------|
| 找 **最短** subarray, sum **≥ target** | `while total >= target` | 已滿足，試著縮小 |
| 找 **最長** substring, **at most k** 個 X | `while count > k` | 超過限制，要縮小 |
| 找 **最長** substring, **without** repeating | `while char in seen` | 有重複，不合法 |

### 💡 記憶口訣
```
題目說「at most k」 → while xxx > k
題目說「>= target」且找最短 → while xxx >= target
題目說「without xxx」 → while 有 xxx
```

---

## 思考流程

###  四步驟框架（每次都套用！）
```
1. Window 內要統計什麼？
   → total / zeros / count / seen

2. R 擴張時要做什麼？
   → total += arr[right]
   → seen.add(arr[right])
   → count[char] += 1

3. 【關鍵】什麼時候 window「太大/不合法」，要收縮 L？
   → 看題目要求！
   → 套用上面的「while 條件」決策表

4. L 收縮時要做什麼？
   → total -= arr[left]
   → seen.remove(arr[left])
   → count[char] -= 1
```

###  實戰例子

**題目：找最短 subarray，sum ≥ target**
```
1. Window 內統計什麼？
   → total (總和)

2. R 擴張時做什麼？
   → total += nums[right]

3. 什麼時候收縮？
   → while total >= target
   （因為已滿足，要試著找更短的）

4. L 收縮時做什麼？
   → total -= nums[left]
```


---

## 常見模板


### 模板 1：找最長 subarray/substring（可變窗口）
 **目標：** 找最長 subarray / substring  
 **核心：** 條件不滿足時才收縮  
 **常用結構：** `HashSet`（不重複） / `HashMap`（次數、distinct）

```python
def longest_window(arr):
    left = 0
    window_state = 初始值  # set / dict / count / sum
    best = 0

    for right in range(len(arr)):
        # 1. 擴張窗口
        window_state = 加入(arr[right])

        # 2. 條件不滿足 → 收縮
        while 條件不滿足:
            window_state = 移除(arr[left])
            left += 1

        # 3. 更新最長長度
        best = max(best, right - left + 1)

    return best

```

#### 適用題目
- Longest Substring Without Repeating Characters
- Max Consecutive Ones III
- Longest Repeating Character Replacement
- Fruit Into Baskets
- Longest Substring with At Most K Distinct Characters

---

### 模板 2：找最短 subarray/substring（可變窗口）
 **目標：** 找最短 subarray / substring                   
 **核心：** 條件「一滿足就縮」                            
 **常用結構：** HashMap（次數、distinct）

```python
def shortest_window(arr):
    left = 0
    window_state = 初始值  # sum / dict
    best = float('inf')

    for right in range(len(arr)):
        # 1. 擴張窗口
        window_state = 加入(arr[right])

        # 2. 條件滿足 → 持續收縮
        while 條件滿足:
            best = min(best, right - left + 1)
            window_state = 移除(arr[left])
            left += 1

    return 0 if best == float('inf') else best

```

#### 適用題目
- Minimum Size Subarray Sum
- Minimum Window Substring

---

### 模板 3：固定大小窗口
 **目標：** 每次只看長度 = k 的窗口                     
 **核心：** right ≥ k - 1 時開始計算             
 **常用結構：** 變數 / HashMap / Deque

```python
def fixed_window(arr, k):
    window_state = 初始值
    best = 初始值
    
    for right in range(len(arr)):
        # 1. 加入 right
        window_state = 更新邏輯(arr[right])
        
        # 2. 當窗口大小達到 k
        if right >= k - 1:
            # 更新答案
            best = 更新(best, window_state)
            
            # 移除 left（保持窗口大小 = k）
            window_state = 移除邏輯(arr[right - k + 1])
    
    return best
```

#### 適用題目
- Maximum Average Subarray I
- Sliding Window Maximum
- Find All Anagrams in String
- Permutation in String

---

### 模板 4：計數型（不求長度，求個數）
**目標：**  不求長度，求「有多少個 subarray」              
**核心：** 每個 right 都能貢獻 right - left + 1          
**常用結構：** 變數（sum / product）或 HashMap

```python
def count_window(arr):
    left = 0
    window_state = 初始值
    count = 0

    for right in range(len(arr)):
        # 1. 擴張窗口
        window_state = 加入(arr[right])

        # 2. 條件不滿足 → 收縮
        while 條件不滿足:
            window_state = 移除(arr[left])
            left += 1

        # 3. 計數
        count += right - left + 1

    return count

```

#### 適用題目
- Subarray Product Less Than K
- Count Number of Nice Subarrays

---



## 練習題單(Problems)


### 📝 Easy（5 題）

| # | 題目 | 難度 | 類型 | 連結 |
|---|------|------|------|------|
| 1 | Maximum Average Subarray I | Easy | 固定窗口 | [LeetCode 643](https://leetcode.com/problems/maximum-average-subarray-i/) |
| 2 | Minimum Size Subarray Sum | Easy | 可變窗口 | [LeetCode 209](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 3 | Max Consecutive Ones III | Easy | K 次容錯 | [LeetCode 1004](https://leetcode.com/problems/max-consecutive-ones-iii/) |



---

### 📝 Medium（7 題）

| # | 題目 | 難度 | 類型 | 連結 |
|---|------|------|------|------|
| 4 | Longest Substring Without Repeating Characters | Medium | HashSet | [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 5 | Fruit Into Baskets | Medium | HashMap（≤2 distinct） | [LeetCode 904](https://leetcode.com/problems/fruit-into-baskets/) |
| 6 | Longest Repeating Character Replacement | Medium | 計數進階 | [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| 7 | Permutation in String | Medium | 固定窗口 | [LeetCode 567](https://leetcode.com/problems/permutation-in-string/) |
| 8 | Find All Anagrams in String | Medium | 固定窗口 | [LeetCode 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |
| 9 | Longest Substring with At Most K Distinct Characters | Medium | HashMap | [LeetCode 340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| 10 | Subarray Product Less Than K | Medium | 總積 | [LeetCode 713](https://leetcode.com/problems/subarray-product-less-than-k/) |

---

### 📝 Hard（3 題）

| # | 題目 | 難度 | 類型 | 連結 |
|---|------|------|------|------|
| 11 | Minimum Window Substring | Hard | HashMap 進階 | [LeetCode 76](https://leetcode.com/problems/minimum-window-substring/) |
| 12 | Sliding Window Maximum | Hard | Deque | [LeetCode 239](https://leetcode.com/problems/sliding-window-maximum/) |
| 13 | Subarrays with K Different Integers | Hard | 轉換技巧 | [LeetCode 992](https://leetcode.com/problems/subarrays-with-k-different-integers/) |

---



## 🎯 時間/空間複雜度

| 情況 | 時間複雜度 | 空間複雜度 |
|------|-----------|-----------|
| 基本 Sliding Window | O(n) | O(1) 或 O(k) |
| 使用 HashSet | O(n) | O(min(n, m)) |
| 使用 HashMap | O(n) | O(k) |
| 固定窗口 | O(n) | O(1) |

**注意：** 雖然有 while 迴圈，但 left 最多移動 n 次，所以總時間仍是 O(n)

---

