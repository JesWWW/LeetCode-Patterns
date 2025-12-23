# LeetCode 643 – Maximum Average Subarray I
🔗 [LeetCode 643 – Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)


- Time: **O(n)** 
- Space: **O(1)**
---

## 1. Understand（理解題意）

確認這題在問什麼，並釐清邊界條件。

**題目：** 長度「剛好等於 k」的連續子陣列中，平均值最大的那一個。  
因為 `k` 固定，其實就是在找：**長度為 k 的 subarray，sum 最大**。

**重點限制：**
- 子陣列一定要是連續
- 長度一定是 `k`

**Clarifying Questions：**
- `nums` 會不會是空？→ 不會
- `k` 一定 ≤ `len(nums)`？→ 是
- `nums` 會有負數？→ 會
- 要輸出什麼？→ 最大平均值（float）

**Test Cases：**
- Happy case:
  - `nums = [1, 12, -5, -6, 50, 3], k = 4`
  - → subarray `[12, -5, -6, 50]` 平均值最大
- Edge cases:
  - 全部都是負數
  - `k = 1`

---

## 2. Match（對應演算法）

**直覺解法：**
- 對每個長度 `k` 的 subarray 都重新算 sum
- Time: **O(nk)**

**優化解法：Sliding Window（固定大小）**

**為什麼選這個解法？**
- 看到關鍵字 subarray
- 視窗大小固定是 `k`
- 每次只會「加一個、減一個」
- 👉 典型固定大小 Sliding Window

---

## 3. Plan（解題規劃）

不要急著寫 Code，先寫 Pseudocode / 邏輯步驟。

1. 用 `total` 存目前 window 的總和
2. 先把前 `k` 個加起來，得到初始 `total`，並設 `best = total`
3. 從 index `k` 開始往右滑：
   - `total += nums[i]`（加右邊新進來的）
   - `total -= nums[i-k]`（減左邊滑出去的）
   - 更新 `best = max(best, total)`
4. 回傳 `best / k`

---

## 4. Implement Code（實作）

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        best = total

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            best = max(best, total)

        return best / k
