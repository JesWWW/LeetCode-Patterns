# Linked List Pointer Manipulation 完全指南

> 透過「不斷鏈」的 invariant，把改指標變成可控流程

---

## 什麼是 Linked List Pointer Manipulation？

**Linked List Pointer Manipulation** 是一類題型：你不是在改 value，而是在改 `next`（或 `random`）指向，重新連接整條鏈結。

它的困難點不在語法，而在於：**一旦指標改錯，你會斷鏈、丟節點、或造出 cycle**。

---

## 核心概念

### Invariant

```
在任何操作過程中，linked list 的 pointer 關係都不能被破壞。
```

這句話是本 Pattern 的核心 invariant。

把它落地成 3 個「每一步都要過」的檢查點：

* **不丟尾巴**：改 `cur.next` 前，一律先存 `nxt = cur.next`
* **不斷鏈**：任何時刻都要能從某個 anchor（dummy 或 head）走到已完成區段
* **不造 cycle**：重接時確認 tail 的 `next` 指回去的位置是你想要的

---

## 何時使用？

### Recognition Cues（看到就該想這個 Pattern）

* 題目要你 **改 linked list 結構**（不是改值）
* 關鍵字：`reverse`, `rotate`, `partition`, `remove`, `cycle`, `random pointer`, `k-group`
* 需要「刪除/插入節點」且會動到 head（通常需要 dummy）

---

## 為什麼這套方法一定可行？

因為所有 linked list manipulation 都可以抽象成：

* **切割（split）**：把 list 拆成幾段
* **局部重排（relink）**：在段內 reverse / 跳過 / 重接
* **接回（reconnect）**：把段與段重新連起來

只要你維持 invariant（不斷鏈、不丟尾巴、不造 cycle），每一步都可驗證正確性。

---

## 思考流程（每次都照問）

```
1) 我要改誰的 next？
2) 改之前，我有沒有先把 nxt 存起來？
3) 我手上是否握有「每一段的 head / tail」？
4) 這一步做完後，anchor（dummy/head）還能走到結果嗎？
5) 下一步移動哪個 pointer？為什麼？
```

---

## Decision Rules（決策規則）

* 只要題目可能影響 head（刪第一個、反轉從 head 開始、分段接回）→ **先上 dummy**
* 只要你要反轉一段 → **先把「尾巴」存起來（nxt）再改 next**
* 只要你要「最終接回」→ 必須同時掌握：

  * 反轉段前一個節點（prev_of_segment）
  * 反轉段的 head / tail
  * 反轉段後的下一段 head
* cycle 題 → 用 fast/slow，並把 while 條件寫成 `while fast and fast.next`

---

## 常見模板

> 你要背的是「pointer 的語意」，不是死背 code。

### 模板 1：Dummy Node（避免 head 特判）

**適用**：remove / partition / reverse II 接回 / k-group 接回

```python
def with_dummy(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # prev 永遠指向「已完成區段」的尾巴
    cur = head
    return dummy, prev, cur
```

**KEY**

* dummy 讓「刪除/插入 head」跟「刪除/插入中間」完全同一套流程

---

### 模板 2：Reverse 一段（標準三指標）

**適用**：Reverse Linked List II、k-group 內部反轉

```python
def reverse_segment(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next      # 不丟尾巴
        cur.next = prev     # 改指向
        prev = cur
        cur = nxt
    return prev
```

**Invariant**

* `prev` 是已反轉好的 head
* `cur` 是待處理的 head

---

### 模板 3：Fast / Slow（Cycle / 追及）

**適用**：Linked List Cycle（是否有 cycle）

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**KEY**

* while 條件必須保證 `fast.next` 可用

---

### 模板 4：Split → Reconnect（分段重接）

**適用**：Rotate List、Partition List、k-group 的「接回」

思考框架：

* Split：找到切點，切成 A 段與 B 段
* Reconnect：把 A.tail 接到 B.head；把 B.tail 接到 A.head（或依題意）

你不一定要先寫出完整 code，但你必須能說清楚：

* 切點在哪（怎麼找到）
* A/B 的 head/tail 是誰
* 最後接回的方向

---

## Common Mistakes（高頻踩雷）

* 先改 `cur.next` 才存 `nxt` → 直接丟掉後半段
* 忘記 dummy → head 需要特判，分支爆炸
* 反轉段接回順序錯（prev/cur/next 的語意沒對齊）
* cycle 題 while 條件寫錯，造成 None dereference
* reconnect 少接一段 → 結果鏈斷掉或尾巴遺失

---

## 面試可用講法（30 秒）

* 「這題是 Linked List pointer manipulation。」
* 「我會用 invariant 保證不斷鏈：改 next 前先存 nxt，並用 dummy 避免 head 特判。」
* 「流程是 split / relink / reconnect；每一步都能從 dummy 走到目前結果。」

---

## 練習題單（Top Interview 150 專屬）

以下題目必須只用你的 Top Interview 150 分類表（Linked List Pointer Manipulation 區塊）。

| # | 題目                                                                                                            | 難度     | 主練點               |
| - | ------------------------------------------------------------------------------------------------------------- | ------ | ----------------- |
| 1 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)                                         | Easy   | Fast/Slow         |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                             | Medium | 建新鏈 + carry       |
| 3 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)                 | Medium | 多指標一致性            |
| 4 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)                               | Medium | 區間反轉 + 接回         |
| 5 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)                           | Hard   | 分段反轉 + 接回         |
| 6 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Medium | dummy + 跳過一段      |
| 7 | [Rotate List](https://leetcode.com/problems/rotate-list/)                                                     | Medium | split + reconnect |
| 8 | [Partition List](https://leetcode.com/problems/partition-list/)                                               | Medium | 兩條鏈分流再接回          |

---

## 建議練習順序（讓你更快內化 invariant）

* 先練「不斷鏈」基本功：

  * Linked List Cycle → Reverse Linked List II → Remove Duplicates II
* 再練「分段重接」：

  * Partition List → Rotate List
* 最後練「組合拳」：

  * k-Group → Random Pointer

---


