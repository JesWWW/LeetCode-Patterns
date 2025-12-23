# LeetCode 704 – Binary Search
🔗 [LeetCode 704 – Binary Search](https://leetcode.com/problems/binary-search/)


- Time: **O(log n)**
- Space: **O(1)**
---

## 1. Understand（理解題意）

**題目：**  
這題要在一個已排序的整數陣列 `nums` 中，搜尋指定的 `target`，如果存在就回傳其index，否則回傳 `-1`。  

**重點限制：**  
- 輸入陣列已排序（升冪）。  
- 搜尋的是單一目標值。  
- 回傳型別為整數索引或 `-1`。  
- 陣列長度可能為 0。

**Clarifying Questions：**  
- Q：陣列是否有排序？ → A：是
- Q：找不到目標時要回傳什麼？ → A：回傳 `-1`。  

**Test Cases：**  
以下列出典型測資與邊界情況，用來驗證解法正確性。  
- Happy case：`nums = [-1,0,3,5,9,12], target = 9`，輸出 `4`。  
- Edge cases：  
  - `nums = [], target = 1` → `-1`  
  - `nums = [5], target = 5` → `0`  
  - `nums = [5], target = 3` → `-1`  
  - `nums = [1,2,3,4], target = 1`（最左）→ `0`  
  - `nums = [1,2,3,4], target = 4`（最右）→ `3`  

---

## 2. Match（對應演算法）
**直覺解法：**  
線性掃描整個陣列，逐一比較每個元素是否等於 `target`，時間複雜度為 `O(n)`。

**優化解法：**  
使用 Binary Search

**為什麼選這個解法？**
- 陣列已排序，可以透過比較直接排除一半搜尋空間。  
- 每次比較後只保留可能包含答案的那一半區間。  
- 時間複雜度從 `O(n)` 降為 `O(log n)`。

---

## 3. Plan（解題規劃）
1. 設定左右指標 `L` 與 `R`，分別指向陣列的起點與終點。  
2. 在 `L <= R` 的條件下重複搜尋。  
3. 每次計算中間index `mid`。  
4. 比較 `nums[mid]` 與 `target`：  
  - 若相等，直接return `mid`。  
  - 若 `nums[mid]` 小於 `target`，代表目標在右半，更新 `L = mid + 1`。  
  - 若 `nums[mid]` 大於 `target`，代表目標在左半，更新 `R = mid - 1`。  
- 若迴圈結束仍未找到，return `-1`。

---

## 4. Implement Code（實作）
```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L, R = 0, n - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid

        return -1
