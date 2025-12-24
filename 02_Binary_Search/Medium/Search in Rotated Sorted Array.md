# LeetCode 33 – Search in Rotated Sorted Array
🔗 [LeetCode 33 – Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)


- Time: **O(log n)**
- Space: **O(1)**

---

## 1. Understand（理解題意）
這題給定一個「原本已經排序、但被旋轉過一次」的整數陣列 `nums`，以及一個目標值 `target`，需要在陣列中找到 `target` 的索引；若不存在則回傳 `-1`。  
其為在「局部有序、整體不完全有序」的結構中，仍然要能每一步排除一半不可能的搜尋空間。

**重點限制：**陣列不是完全排序但只被旋轉一次、元素互不重複、必須回傳索引或 `-1`、要求時間複雜度為 `O(log n)`。

**Clarifying Questions：**
- Q：陣列是否可能為空？ → A：是，空陣列直接回傳 `-1`。  
- Q：陣列是否一定只旋轉一次？ → A：是，最多只存在一個 pivot。  
- Q：元素是否會重複？ → A：不會，本題假設元素皆唯一。

**Test Cases：**  
- Happy case：`nums = [4,5,6,7,0,1,2], target = 0` → `4`  
- Edge cases：  
  - `nums = [], target = 3` → `-1`  
  - `nums = [1], target = 1` → `0`  
  - `nums = [1], target = 0` → `-1`  
  - `nums = [3,1], target = 1` → `1`  

---

## 2. Match（對應演算法）
**直覺解法：**
- Brute Force ，線性掃描整個陣列，比對每個元素是否等於 `target`
- Time: **O(n)** 

**優化解法：Binary Search 的變形（Rotated Binary Search）**
- 在每一次比較時，判斷左半或右半哪一邊是有序的，再利用有序區間進行範圍判斷。

**為什麼選這個解法？**
- 陣列雖然被旋轉，但至少有一半仍有序。  
- 可以利用排序區間來安全地排除一半搜尋空間。  
- 符合題目對 `O(log n)` 時間複雜度的要求。

---

## 3. Plan（解題規劃）
1. 初始化左右指標 `L = 0`、`R = n - 1`
2. 在 `L <= R` 的情況下重複搜尋，計算中間索引 `mid`。  
3. 若 `nums[mid] == target`，直接回傳 `mid`。  
4. 判斷哪一半是有序的：  
   - 若 `nums[L] <= nums[mid]`，代表左半 `[L .. mid]` 有序。  
   - 否則右半 `[mid .. R]` 有序。  
5. 若左半有序，檢查 `target` 是否落在 `[nums[L], nums[mid])` 範圍內，決定保留左半或右半。  
6. 若右半有序，檢查 `target` 是否落在 `(nums[mid], nums[R]]` 範圍內，決定保留右半或左半。  
7. 持續縮小搜尋區間，直到找到答案或區間為空。

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

            if nums[mid] == target:
                return mid

            # 左半有序
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            # 右半有序
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1

        return -1
