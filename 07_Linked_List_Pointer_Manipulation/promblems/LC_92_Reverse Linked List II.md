# LeetCode 92 – Reverse Linked List II

🔗 [Problem Link](https://leetcode.com/problems/reverse-linked-list-ii/)

**Pattern**: Linked List Pointer Manipulation
**Difficulty**: Medium
**Time**: O(n) | **Space**: O(1)

---

## U - Understand

**問題**: 只反轉 linked list 中從 `left` 到 `right` 的那一段，其他部分保持原順序。

**限制**:

* 只反轉一段，不是整條 list
* 需要原地調整 pointer
* `left` 可能等於 `1`
* `left == right` 時其實不用改

**KEY**:
這題不是單純 reverse whole list，而是：

1. 找到反轉區間前一個節點
2. 反轉中間這段
3. 把前後兩段重新接回去

**Test Cases**:

```python
head = [1,2,3,4,5], left = 2, right = 4
# output: [1,4,3,2,5]

head = [5], left = 1, right = 1
# output: [5]
```

---

## M - Match

### 我一開始的想法

我先想到：

1. 走到 `left` 前一個位置
2. 記住反轉前的起點
3. 開始做 pointer reverse
4. 最後把反轉後的區間接回去

這個大方向其實是對的。
我已經知道這題的核心不是值交換，而是 pointer manipulation。

### 我卡住的地方

我一開始覺得很怪，因為腦中同時有很多角色：

* `before`
* `first`
* `prev`
* `curr`
* `nxt`

所以很容易把不同階段的 pointer 混在一起。

### 我原本邏輯中正確的地方

* 知道要先找到 `left` 前一個節點
* 知道要記住反轉區間的第一個節點
* 知道反轉後要把區間重新接回原 list

### 我原本邏輯中錯的地方

1. **把不同角色的 `prev` 混在一起**

   * 一開始會把「區間前一個節點」和「reverse 過程中的 prev」想成同一個東西
   * 其實它們是兩個不同角色

2. **reverse loop 的 invariant 不夠穩**

   * 如果 `prev` 起始不是 `None`
   * 或 `curr` 更新不是用 `nxt`
   * pointer 很容易直接壞掉

3. **最後 return 錯了**

   * 如果用了 `dummy`，最後應該回傳 `dummy.next`
   * 不是原本的 `head`

### 正確 Pattern

這題屬於 **Linked List Pointer Manipulation**。
關鍵不是背模板，而是守住這個 invariant：

> 在任何操作過程中，linked list 的 pointer 關係都不能被破壞。

---

## P - Plan

### 核心想法

把整條 list 看成三段：

```text
前段 -> 反轉區間 -> 後段
```

我們只需要：

1. 找到反轉區間前一個節點 `before`
2. 找到反轉區間第一個節點 `first`
3. 反轉 `right - left + 1` 個節點
4. 最後接兩條線：

   * `before.next = prev`
   * `first.next = curr`

---

### 為什麼需要 dummy？

如果 `left = 1`，那反轉區間是從 head 開始。
這時候真正的「前一個節點」不存在。

所以先建立：

```python
dummy = ListNode(0, head)
```

這樣就能統一處理：

* `left = 1`
* `left > 1`

也就是說：

> `before` 不是永遠等於 dummy，
> 而是從 dummy 出發，走到 `left` 前一個位置。

---

### Invariant

#### 區間外的 invariant

* `before` 永遠指向反轉區間前一個節點
* `first` 永遠是反轉區間原本的第一個節點
  反轉完成後，它會變成這段的尾巴

#### reverse 過程中的 invariant

* `prev` = 已反轉部分的頭
* `curr` = 下一個待反轉節點

每一輪固定操作都是：

```text
1. 暫存 nxt = curr.next
2. curr.next = prev
3. prev = curr
4. curr = nxt
```

這就是這題真正的不變操作。

---

### Step-by-step

```text
1. 建立 dummy，讓 before 一定存在
2. 讓 before 走到 left 前一個節點
3. first = before.next
4. 從 first 開始做局部 reverse，共 right-left+1 次
5. 反轉完成後：
   - before.next = prev
   - first.next = curr
6. 回傳 dummy.next
```

---

## I - Implement

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        before = dummy

        # Move before to the node before position left
        for _ in range(left - 1):
            before = before.next

        first = before.next
        prev = None
        curr = first
        rev = right - left + 1

        # Reverse the interval [left, right]
        while rev and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            rev -= 1

        # Reconnect
        before.next = prev
        first.next = curr

        return dummy.next
```

---

## R - Review

**Complexity**:

* Time: O(n)

  * 最多走整條 list 一次
* Space: O(1)

  * 只用固定幾個 pointer

**為什麼是 O(n)**:

* 先走到 `left - 1`
* 再反轉 `right - left + 1`
* 沒有重複掃描整段 many times

---

## E - Evaluate

**Edge Cases**:

* `left == right` ✓
* `left = 1` ✓
* 只有一個節點 ✓
* 反轉整條 list ✓

**Notes**:

* 一開始我知道要「找到前一段、反轉中間、接回去」，方向是對的
* 真正卡住的是沒有把「區間外角色」和「區間內 reverse 流程」分開思考
* `dummy` 的作用不是答案本身，而是讓 `left = 1` 時也能有一個合法的 `before`

**Common Errors**:

* 把 `before` 和 reverse 中的 `prev` 混在一起
* `prev` 一開始不是 `None`
* 忘記先存 `nxt`
* 寫成 `curr = curr.next`，導致走錯方向
* 最後回傳 `head` 而不是 `dummy.next`

---

## What I Learned

這題最重要的不是「會不會 reverse linked list」，而是：

> 要把「局部 reverse」和「前後接回去」分成兩個階段思考。

如果直接把所有 pointer 混在一起，很容易覺得題目很怪。
但一旦固定角色：

* `before`：反轉區間前一個節點
* `first`：反轉區間原本第一個節點
* `prev`：已反轉部分的頭
* `curr`：下一個待反轉節點

整題就會變得很清楚。

這題也讓我更確定一件事：

> Linked list 題不是背 case，
> 而是先固定每個 pointer 的語意，再守住 loop invariant。
