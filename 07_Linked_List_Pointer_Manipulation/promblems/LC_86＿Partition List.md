# LeetCode 86 – Partition List

🔗 [Problem Link](https://leetcode.com/problems/partition-list/)

**Pattern**: Linked List Pointer Manipulation
**Difficulty**: Medium
**Time**: O(n) | **Space**: O(1)

---

## U - Understand

**問題**: 給一條 linked list 和一個值 `x`，把所有 `< x` 的節點放到前面，所有 `>= x` 的節點放到後面。

**重點**:

* 這不是排序
* 只是在做 partition
* 必須保留原本的相對順序

也就是說：

* 所有 `< x` 的節點之間，順序不能亂
* 所有 `>= x` 的節點之間，順序也不能亂

**例子**:

```python
head = [1,4,3,2,5,2], x = 3
# output: [1,2,2,4,3,5]
```

---

## M - Match

### 一開始的直覺想法

我一開始想到的是：

1. 掃描整條 list
2. 如果 `curr.val < x`，就把這個 node 搬到前面
3. 同時把原本的 `next` 接回去，避免斷鏈

這個方向不是完全錯，因為我已經知道：

* 題目要求的是 pointer 操作，不是值交換
* 也知道操作 node 前要先存 `next`

### 我原本思路中正確的地方

* 知道這題是 linked list pointer manipulation
* 知道這題不是 sort，只是依條件分組
* 知道要先存 `curr.next`，不然移動 node 時容易斷鏈

### 我原本思路中錯的地方

#### 1. 想直接在原串列中「搬 node」

這會立刻遇到兩個問題：

* 誰把這個 node 從原位置摘掉？
* 誰把這個 node 接到新位置？

如果這兩件事沒有明確維護，pointer 很容易壞掉。

#### 2. `new_curr = head` 的角色不穩

如果 `head.val >= x`，那它根本不應該是 `< x` 區塊的尾巴。
所以這種初始化方式沒有穩定的語意。

#### 3. 沒有自然保證 stable partition

這題不是只要把 `< x` 放前面就好，還要保留相對順序。
如果邊掃邊插、邊從原串列中間搬移，順序很容易亂掉。

### 正確 Pattern

這題屬於 **Linked List Pointer Manipulation**。
更穩的模型不是「把某個 node 搬到前面」，而是：

> 一邊掃描，一邊把節點分配到兩條結果串列中。

---

## P - Plan

### 核心想法

建立兩條 linked list：

* `less`：存所有 `< x` 的節點
* `greater`：存所有 `>= x` 的節點

最後再把兩條接起來。

這樣的好處是：

* 不需要在原串列中間做危險的插拔
* 每個 node 只會被處理一次
* 可以自然保留相對順序

---

### Invariant

在任何時候：

* `dummy1 -> ... -> tail1` 永遠只包含所有已處理且 `< x` 的節點
* `dummy2 -> ... -> tail2` 永遠只包含所有已處理且 `>= x` 的節點
* 兩條串列內部的順序都和原 linked list 一致

這題的關鍵不是「怎麼搬」，而是：

> 每個節點都只做一次分類：接到 `less` 或 `greater` 的尾巴後面。

---

### Step-by-step

```text
1. 建立兩個 dummy nodes：
   - dummy1 for nodes < x
   - dummy2 for nodes >= x

2. 用 curr 掃描原 linked list

3. 每輪先存 nxt = curr.next
   - 因為等一下會改 curr.next

4. 如果 curr.val < x：
   - 接到 tail1 後面
   - tail1 前進

5. 否則：
   - 接到 tail2 後面
   - tail2 前進

6. curr = nxt，繼續掃描

7. 最後把兩條串列接起來：
   - tail1.next = dummy2.next

8. 回傳 dummy1.next
```

---

## I - Implement

```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        tail1 = dummy1
        tail2 = dummy2
        curr = head

        while curr:
            nxt = curr.next

            if curr.val < x:
                tail1.next = curr
                tail1 = tail1.next
            else:
                tail2.next = curr
                tail2 = tail2.next

            curr = nxt

        tail1.next = dummy2.next
        return dummy1.next
```

---

## R - Review

### Complexity

* **Time**: O(n)
* **Space**: O(1)

### 為什麼是 O(n)

每個節點只會被訪問一次，並且只會被接到某一條結果串列一次。

---

## E - Evaluate

### Edge Cases

* `head = None` ✓
* 全部節點都 `< x` ✓
* 全部節點都 `>= x` ✓
* `< x` 和 `>= x` 交錯出現 ✓
* 只有一個節點 ✓

---

### 我原本思路中最值得修正的地方

我一開始比較像在想：

> 能不能把某個 `< x` 的 node 直接搬到前面？

但這種思路會讓我陷入：

* 要怎麼摘下來？
* 要怎麼插回去？
* 要怎麼不破壞原本順序？

更好的思路是：

> 不搬來搬去，而是把每個節點分配到兩條結果串列之一。

這樣每輪的操作就非常固定，也更不容易寫錯。

---

### Common Errors

#### 1. 接上去後忘記移動 tail

例如只寫：

```python
tail1.next = curr
```

卻沒寫：

```python
tail1 = tail1.next
```

這樣下一輪會覆蓋掉前面接過的節點。

#### 2. 忘記先存 `nxt`

如果先改了 `curr.next`，卻沒先存原本下一個節點，後面就沒辦法繼續遍歷原串列。

#### 3. 忘記把 `curr.next = None`

這不是每題都絕對必要，但這題重用原節點時，先切斷舊鏈會讓結構更乾淨，也更容易保證 invariant。

#### 4. 想直接在原串列中間做插拔

這通常比兩條串列法更容易出錯，尤其是在維護順序時。

---

## What I Learned

這題讓我更清楚一件事：

> Linked list 題很多時候不是「我能不能把這個 node 搬到某個地方」，
> 而是「我能不能把每個 node 穩定地分配到正確的結果結構裡」。

我一開始的想法已經碰到正確方向的一部分：

* 要改 pointer
* 要先存 `next`

但還停留在局部搬移節點。
真正更穩的做法是建立兩條串列，讓每輪操作都變成固定的分類動作。

這題的核心不是技巧多，而是 invariant 要夠清楚：

> `less` 和 `greater` 永遠都是已處理節點的穩定分區結果。
