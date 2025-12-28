# Two Pointers 完全指南

> 透過 pointer 移動邏輯縮小搜尋空間

---

## 什麼是 Two Pointers？

**Two Pointers** 是一種使用兩個 pointer 在陣列或序列中移動，透過每次移動其中一個 pointer 來縮小搜尋空間的技巧。

### 核心思想

- 使用兩個 pointer（通常命名為 L、R 或 i、j）
- 根據當前狀態決定移動哪個 pointer
- 每次移動都能**排除一部分不可能的解**
- 避免暴力法的 O(n²) 時間複雜度

---

## 何時使用？

### 適用場景

| 關鍵特徵 | 範例題型 |
|---------|---------|
| sorted array | Two Sum II、3Sum |
| 需要 in-place 操作 | Remove Duplicates、Remove Element |
| pair/triplet 配對問題 | Container With Most Water、3Sum |
| palindrome 檢查 | Valid Palindrome |
| 合併兩個序列 | Merge Sorted Array、Merge Two Sorted Lists |
| 快慢指標 | Linked List Cycle、Remove Nth Node |

### 判斷口訣

1. 陣列有序嗎？（通常需要）
2. 需要配對或比較嗎？
3. 能透過 pointer 移動排除解嗎？

---

## 核心概念

### Invariant

```
每一次移動其中一個 pointer，都能在不漏解的情況下縮小搜尋範圍
```

關鍵：必須能證明被排除的部分「不可能包含答案」

### Two Pointers 的三種形式

#### 1. 對撞型（Opposite Direction）

兩個 pointer 從兩端向中間移動

```
[1, 2, 3, 4, 5, 6]
 L              R
    L        R
       L  R
```

**適用**：sorted array、配對問題、palindrome

#### 2. 同向型（Same Direction）

兩個 pointer 從同一端出發，速度不同

```
[1, 2, 3, 4, 5, 6]
 S  F               (slow, fast)
    S     F
       S        F
```

**適用**：快慢指標、in-place 操作、區間問題

#### 3. 雙序列型（Two Sequences）

兩個 pointer 分別在不同陣列/linked list 上移動

```
arr1: [1, 3, 5]
       i
arr2: [2, 4, 6]
       j
```

**適用**：merge、intersection、subsequence

---

## 思考流程

每次都問這些問題：

```
1. 初始位置在哪？
   - 兩端 (L=0, R=n-1)
   - 同起點 (slow=0, fast=0)
   - 各自序列起點

2. 移動條件是什麼？
   - 什麼情況移動 L？
   - 什麼情況移動 R？
   - 能否同時移動？

3. 終止條件是什麼？
   - L < R
   - L <= R  
   - fast 到底

4. 移動後 invariant 還成立嗎？
   - 被排除的部分真的不可能是答案嗎？
```

---

## 常見模板

### 模板 1：對撞型（Sorted Array）

**適用**：在 sorted array 中找配對

```python
def two_pointers_opposite(nums, target):
    L, R = 0, len(nums) - 1
    
    while L < R:
        current = nums[L] + nums[R]
        
        if current == target:
            return [L, R]
        elif current < target:
            L += 1  # 和太小，左邊往右移
        else:
            R -= 1  # 和太大，右邊往左移
    
    return []
```

**關鍵決策**：
- `current < target` → 只能移動 L（移動 R 只會更小）
- `current > target` → 只能移動 R（移動 L 只會更大）

**適用題目**：
- Two Sum II (LeetCode 167)
- 3Sum (LeetCode 15)
- Container With Most Water (LeetCode 11)
- Trapping Rain Water (LeetCode 42)

---

### 模板 2：同向型（In-place Modification）

**適用**：需要 in-place 修改陣列

```python
def two_pointers_same_direction(nums):
    slow = 0  # 慢指標：下一個有效位置
    
    for fast in range(len(nums)):
        if 滿足條件(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1
    
    return slow  # 新的長度
```

**關鍵概念**：
- **slow**：下一個可以放入有效元素的位置
- **fast**：掃描整個陣列
- **invariant**：`[0, slow)` 內都是有效元素

**適用題目**：
- Remove Element (LeetCode 27)
- Remove Duplicates from Sorted Array (LeetCode 26)
- Remove Duplicates from Sorted Array II (LeetCode 80)

---

### 模板 3：快慢指標（Linked List）

**適用**：Linked List 問題

```python
def fast_slow_pointers(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # 有 cycle
    
    return False
```

**關鍵性質**：
- fast 走兩步，slow 走一步
- 若有 cycle，必定會相遇
- 相遇點到 cycle 起點距離 = head 到 cycle 起點距離

**適用題目**：
- Linked List Cycle (LeetCode 141)
- Remove Nth Node From End (LeetCode 19)

---

### 模板 4：雙序列合併

**適用**：合併兩個有序序列

```python
def merge_two_sequences(arr1, arr2):
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # 處理剩餘元素
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
```

**KEY**：
- 比較當前元素，選較小的
- 移動被選中的 pointer
- 最後處理剩餘部分

**適用題目**：
- Merge Sorted Array (LeetCode 88)
- Merge Two Sorted Lists (LeetCode 21)
- Is Subsequence (LeetCode 392)

---

### 模板 5：Palindrome 檢查

**適用**：檢查是否為迴文

```python
def is_palindrome(s):
    L, R = 0, len(s) - 1
    
    while L < R:
        # 跳過非字母數字
        while L < R and not s[L].isalnum():
            L += 1
        while L < R and not s[R].isalnum():
            R -= 1
        
        # 比較
        if s[L].lower() != s[R].lower():
            return False
        
        L += 1
        R -= 1
    
    return True
```

**適用題目**：
- Valid Palindrome (LeetCode 125)

---

## 練習題單

### Problems

| # | 題目 | 難度 | 類型 |
|---|------|------|------|
| 1  | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)       | Easy   | 同向型   |
| 2  | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)                                         | Easy   | 雙序列   |
| 3  | [Remove Element](https://leetcode.com/problems/remove-element/)                                                 | Easy   | 同向型   |
| 4  | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                             | Easy   | 對撞型   |
| 5  | [Is Subsequence](https://leetcode.com/problems/is-subsequence/)                                                 | Easy   | 雙序列   |
| 6  | [Summary Ranges](https://leetcode.com/problems/summary-ranges/)                                                 | Easy   | 同向型   |
| 7  | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)                                   | Medium | 對撞型   |
| 8  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                           | Medium | 對撞型   |
| 9  | [3Sum](https://leetcode.com/problems/3sum/)                                                                     | Medium | 對撞型進階 |
| 10 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Medium | 同向型   |
| 11 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                                       | Hard   | 對撞型進階 |


### Linked List Specific

| # | 題目 | 難度 | 類型 |
|---|------|------|------|
| 1 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | 快慢指標 |
| 2 | [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | 快慢指標 |
| 3 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | 雙序列 |


---

## Complexity

| 情況 | 時間 | 空間 |
|------|------|------|
| 對撞型 | O(n) | O(1) |
| 同向型 | O(n) | O(1) |
| 快慢指標 | O(n) | O(1) |
| 雙序列合併 | O(n + m) | O(1) 或 O(n + m) |

---

## 常見錯誤

### 1. 移動邏輯錯誤

```python
# ❌ 錯誤：無法排除任何解
if nums[L] + nums[R] < target:
    R -= 1  # 錯了！應該移動 L

# ✅ 正確：根據 sorted 特性移動
if nums[L] + nums[R] < target:
    L += 1  # 左邊太小，往右找更大的
```

### 2. 邊界條件處理

```python
# ❌ 錯誤：L = R 時會重複計算
while L <= R:
    ...

# ✅ 正確：根據題意選擇
while L < R:  # 配對問題，不能自己和自己配
    ...
```

### 3. In-place 操作時忘記返回長度

```python
# ❌ 錯誤：只修改了陣列，沒返回新長度
def removeDuplicates(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    # 忘記 return slow

# ✅ 正確
def removeDuplicates(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

---

## 面試技巧

### 說出你的思考過程

1. "我注意到陣列是 sorted 的，可以用 Two Pointers"
2. "我會用對撞型，從兩端往中間移動"
3. "移動規則是：和太小就移動 L，和太大就移動 R"
4. "這樣每次移動都能排除一半，時間複雜度 O(n)"

### 3Sum 的經典思路

```
3Sum = 固定一個數 + 對剩下的做 Two Sum II

for i in range(n):
    target = -nums[i]
    # 對 [i+1, n-1] 做 Two Sum II
    two_pointers(nums, i+1, n-1, target)
```

### Trapping Rain Water 的關鍵觀察

```
積水量取決於：
min(left_max, right_max) - height[i]

用 Two Pointers 維護 left_max 和 right_max
移動較小的那一邊
```

---