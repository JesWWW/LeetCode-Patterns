# LeetCode 61 – Rotate List

🔗 [Problem Link](https://leetcode.com/problems/rotate-list/)

**Pattern**: Linked List Pointer Manipulation
**Difficulty**: Medium
**Time**: O(n) | **Space**: O(1)

---

## U - Understand

**問題**: 給一條 linked list，把整條 list 向右旋轉 `k` 次。

**例子**:

```python
1 -> 2 -> 3 -> 4 -> 5, k = 2
# output: 4 -> 5 -> 1 -> 2 -> 3
```

右旋一次的意思是：

* 最後一個節點搬到最前面

所以右旋兩次就是：

```python
1 -> 2 -> 3 -> 4 -> 5
5 -> 1 -> 2 -> 3 -> 4
4 -> 5 -> 1 -> 2 -> 3
```

**注意**:

* `k` 可能很大
* list 可能為空
* list 可能只有一個節點
* 如果剛好轉整圈，結果不變

---

## M - Match

### 一開始的直覺想法

我一開始想到的是：

1. 每次找到最後一個節點
2. 把它搬到最前面
3. 把這個過程重複做 `k` 次

這個想法在概念上是對的，因為那的確是「右旋一次」。

### 我原本思路中正確的地方

* 知道右旋一次本質上就是把 tail 搬到 head 前面
* 知道需要改 pointer，而不是改值
* 知道 head 會改變

### 我原本思路中不夠好的地方

這個做法如果真的做 `k` 輪，每一輪都要重新掃到尾巴，會變成：

* 每次旋轉 O(n)
* 總共 O(nk)

如果 `k` 很大，會超時。

### 關鍵轉念

這題不需要模擬每一次旋轉。
更好的想法是：

> 先算出最終應該在哪裡斷開，再一次完成旋轉。

### 正確 Pattern

這題屬於 **Linked List Pointer Manipulation**。
重點不是一個節點一個節點搬，而是：

* 先看清楚整體結構
* 再一次改正確的 pointer

---

## P - Plan

### 核心想法

把 linked list 先接成一個環，
那麼右旋 `k` 次，其實就等於：

> 在環上找到新的尾巴，然後把環斷開。

---

### 關鍵觀察

假設 list 長度是 `n`。

#### 1. 右旋 `k` 次，等於右旋 `k % n` 次

因為轉超過一整圈會回到原位。

#### 2. 如果把尾巴接回 head

原本：

```python
1 -> 2 -> 3 -> 4 -> 5
```

接成環後：

```python
1 -> 2 -> 3 -> 4 -> 5
^                   |
|___________________|
```

這時只要找到新的尾巴，斷開即可。

#### 3. 新尾巴在哪裡？

如果右旋 `k` 次：

* 新頭是第 `n - k` 個節點
* 新尾是第 `n - k - 1` 個節點

所以從 `head` 走 `n - k - 1` 步，就能找到新尾巴。

---

### Invariant

這題最重要的 invariant 是：

> 當 linked list 被接成環後，旋轉問題就變成「找新的斷點」。

也就是說：

* 不需要真的旋轉很多次
* 只需要找到哪個節點應該變成新尾巴
* `new_head = new_tail.next`

---

### Step-by-step

```text
1. 處理 edge cases：空 list、單節點、k = 0
2. 先算出 linked list 長度 n，並找到 tail
3. curr.next = head，把整條 list 接成環
4. k %= n
5. 如果 k == 0，代表轉一整圈，直接回傳原 head
6. 從 head 走 n-k-1 步，找到新尾巴
7. 新頭 = 新尾巴.next
8. 把新尾巴.next 設成 None，斷開環
9. 回傳新頭
```

---

## I - Implement

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # edge cases
        if not head or not head.next or k == 0:
            return head

        # Count the length of the list
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head  # make it circular

        # If it turns out to rotate one full cycle
        k %= n
        if k == 0:
            return head
        
        # Find the new tail and head
        tail = head
        for _ in range(n - k - 1):
            tail = tail.next
        head = tail.next
        tail.next = None

        return head
```

---

## R - Review

### Complexity

* **Time**: O(n)
* **Space**: O(1)

### 為什麼是 O(n)

* 算長度一次
* 找新尾巴一次
* 沒有重複做 `k` 次旋轉

---

## E - Evaluate

### 我原本思路中哪裡是對的

我原本已經抓到：

* 右旋的本質和 tail 有關
* 需要改 head
* 需要改 pointer，而不是改值

這些都是正確方向。

### 我原本思路中哪裡錯或不夠完整

#### 1. 把「右旋 k 次」真的做成 k 輪

這會讓時間複雜度變成 O(nk)。

#### 2. 一開始把長度算錯

我之前有一版把 `n` 初始成 `0`，然後用：

```python
while curr.next:
    curr = curr.next
    n += 1
```

這樣算出來的不是節點數，而是邊數，會少一個。

正確做法是：

```python
n = 1
```

因為 head 本身就是第一個節點。

#### 3. 忘了旋轉一整圈等於不變

一定要先做：

```python
k %= n
```

否則會做很多沒必要的操作。

---

## Common Errors

### 1. 真的模擬每一次旋轉

這樣通常會超時。

### 2. 長度 `n` 算成 `n - 1`

這會導致：

* `k %= n` 錯
* 找新尾巴的位置也錯

### 3. 忘記處理 `k % n == 0`

這種情況不需要改 list。

### 4. 找到新頭後忘記斷開環

如果不做：

```python
tail.next = None
```

最後會變成 cycle。

---

## What I Learned

這題讓我更清楚一件事：

> 有些 linked list 題不能一直模擬局部操作，而要先看出最終結構。

我一開始想到的「每次把最後一個節點搬到前面」不是錯，
但它停留在單步操作，沒有往上抽象。

真正更好的想法是：

* 先把 list 接成環
* 再把旋轉問題改寫成找斷點問題

這樣就能把原本 O(nk) 的做法，壓成 O(n)。

這題也再次提醒我：

> 當一個操作會被重複做很多次時，要先問自己能不能直接算出最後位置，而不是逐步模擬。
