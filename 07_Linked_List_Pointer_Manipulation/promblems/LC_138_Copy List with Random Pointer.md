# LeetCode 138 – Copy List with Random Pointer

🔗 [Problem Link](https://leetcode.com/problems/copy-list-with-random-pointer/)

**Pattern**: Linked List Pointer Manipulation + Hashing
**Difficulty**: Medium
**Time**: O(n) | **Space**: O(n)

---

## U - Understand

**問題**: 複製一個 linked list，每個節點除了 `next`，還有一個 `random` 指標。
新的 linked list 必須：

* 節點值相同
* `next` 結構相同
* `random` 結構也相同
* 但所有節點都必須是新的，不能指回舊 linked list

**限制**:

* `random` 可能是 `None`
* `random` 可能指向前面、後面、自己
* 不能只複製值，必須複製 pointer 關係

**Test Cases**:

```python
[[7,None],[13,0],[11,4],[10,2],[1,0]]
# 第一個節點 random = None
# 第二個節點 random 指向 index 0
```

---

## M - Match

### 一開始的直覺想法

先從頭走到尾，建立新的 linked list，複製每個節點的值。
但卡住的地方是：

* `random` 可能指向後面的節點，當下還沒建出來
* 也可能指向前面的節點，或是 `None`
* 如果看到 `random` 就直接新建節點，可能會複製出重複節點，破壞結構

### 哪裡是對的？

這個方向有一半是對的：

* 先走一次，把所有新節點建出來
* 再走第二次補 `random`

這個兩輪想法是正確的。

### 哪裡不夠完整？

問題不在於「要不要分兩輪」，而在於：

> 第二輪要怎麼知道某個舊節點對應到哪個新節點？

這題的關鍵不是 index，也不是值，
而是要建立：

```python
old node -> copied new node
```

### 正確 Pattern

這題本質上是：

* **Linked List Pointer Manipulation**：要正確重建 `next` / `random`
* **Hashing**：要用 O(1) lookup 找到 old node 對應的 new node

---

## P - Plan

### 核心策略：兩輪處理

#### 第一輪

先複製所有節點，建立 `old -> new` 的 mapping，並把 `next` 順序串好。

#### 第二輪

再走一次原 linked list，根據舊節點的 `random`，去 mapping 中找到對應的新節點，補上 `random`。

---

### Invariant

#### 第一輪 invariant

對於所有已訪問過的舊節點 `old`：

```python
copies[old] = copied node
```

也就是說，只要舊節點已經被處理過，我就能立刻找到它對應的新節點。

#### 第二輪 invariant

對於所有已訪問過的舊節點 `old`，其對應的新節點 `copies[old]` 的 `random` 已經被正確設好。

---

### 為什麼這樣可行？

因為第一輪結束後：

* 所有新節點都已存在
* 所有 old node 都能透過 dictionary 找到對應的新節點

所以第二輪只要做這個統一操作：

```python
copies[old].random = copies.get(old.random)
```

如果 `old.random` 是某個舊節點，就找到對應的新節點。
如果 `old.random` 是 `None`，`get(None)` 會直接回傳 `None`。

---

### Step-by-step

```text
1. 建立 dummy node，方便串接新 linked list
2. 第一輪遍歷 old list：
   - 建立新節點
   - copies[old] = new node
   - curr.next = new node
3. 第二輪遍歷 old list：
   - copies[old].random = copies.get(old.random)
4. 回傳 dummy.next
```

---

## I - Implement

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr = dummy
        old = head
        copies = {}

        # First pass: copy nodes and build mapping
        while old:
            curr.next = Node(old.val)
            copies[old] = curr.next
            curr = curr.next
            old = old.next

        # Second pass: assign random pointers
        old = head
        while old:
            copies[old].random = copies.get(old.random)
            old = old.next

        return dummy.next
```

---

## R - Review

**Complexity**:

* Time: O(n)

  * 第一輪走一次
  * 第二輪再走一次
* Space: O(n)

  * dictionary 存每個 old node 對應的新節點

---

## E - Evaluate

### 我原本想法中正確的地方

* 知道這題不能只看值，還要處理 `random`
* 想到可以分兩輪做
* 第一輪先把 `next` 順序處理好，第二輪再補 `random`

### 我原本想法中錯的地方

* 一開始把 `random` 想成和 index 有關
* 想在當下立刻決定 `random` 指向誰
* 有一度想「看到 random 就直接新建節點」，這會破壞一一對應關係

### 真正的關鍵轉念

這題不是：

> random 指到前面怎麼辦？
> random 指到後面怎麼辦？
> random 是 None 怎麼辦？

而是：

> 我如何讓任何 old node 都能在 O(1) 時間找到它對應的新節點？

只要這件事成立，`random` 的所有情況都能被同一條規則統一處理。

---

## Common Errors

* 把節點值當成節點身份，導致 mapping 錯誤
* 看到 `random` 就直接新建節點，造成重複複製
* 用 index 思考，而不是用 node reference 思考
* 寫成 `copies[old.random]`，遇到 `old.random is None` 可能出錯
* 忘記新 linked list 的 `random` 必須指向**新節點**，不能指回舊節點

---

## Notes

* `copies.get(old.random)` 很重要
  因為：

  * 找得到就回傳對應的新節點
  * 找不到（例如 `old.random is None`）就回傳 `None`

* 這題最值得記住的不是 code，而是這個模型：

> 先建立新世界中的所有節點，再用 old -> new mapping 重建 pointer 關係

* 之後遇到 clone graph、copy tree、random pointer 類題，都可以先問自己：

> 舊世界的某個節點，在新世界裡對應到誰？
