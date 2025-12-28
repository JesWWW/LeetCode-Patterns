# Patterns Overview

LeetCode 題目依照**解題 Pattern**系統化整理。

## 核心目標

> **熟練少數幾個 Pattern 與其 invariant，即可無痛解完 LeetCode Top Interview 150。**

---

## 如何使用這個 Repository

每個 Pattern 包含三部分：

- **Lecture**：核心概念、思考流程、常見模板、練習題單
- **Problems**：精選題目筆記
- **Solutions**：參考實作

### 建議使用順序

1. 先讀 Lecture，搞懂 invariant
2. 再解 Problems（刻意練習）
3. 最後對照 Solution 檢查思路

---

## Pattern Index

### 1. Two Pointers

**Invariant**
> 每一次移動其中一個 pointer，都能在不漏解的情況下縮小搜尋範圍。

**常見應用**：sorted array、in-place 操作、pair/triplet 問題

---

### 2. Sliding Window

**Invariant**
> Window 內的狀態永遠代表一個合法或接近合法的解。

**常見應用**：subarray/substring、longest/shortest、at most/exactly K

---

### 3. Binary Search

**Invariant**
> 每一次比較後，都能證明有一半的搜尋空間不可能包含答案。

**常見應用**：sorted/partially sorted array、boundary/minimum/index、O(log n) 題目

---

### 4. Prefix Sum / Accumulation

**Invariant**
> 任意區間的資訊，都可以由兩個 prefix state 相減得到。

**常見應用**：subarray sum/count、range query、product except self

---

### 5. Greedy

**Invariant**
> 當下做出的局部最佳選擇，可以被證明不會影響最終最優解。

**常見應用**：jump/interval 問題、stock 系列、資源分配

---

### 6. Hashing / Frequency Map

**Invariant**
> 題目所需的所有狀態，都可以用 O(1) lookup 的 mapping 表示。

**常見應用**：counting、grouping、existence check

---

### 7. Stack / Monotonic Stack

**Invariant**
> Stack 中的元素必須維持某種順序或巢狀結構。

**常見應用**：parentheses、expression evaluation、next greater/smaller element

---

### 8. Linked List Pointer Manipulation

**Invariant**
> 在任何操作過程中，linked list 的 pointer 關係都不能被破壞。

**常見應用**：reverse、cycle detection、partition

---

### 9. DFS (Tree)

**Invariant**
> 每一個 subtree 本身就是一個完整的子問題。

**常見應用**：tree traversal、path 問題、bottom-up aggregation

---

### 10. BFS (Tree / Graph)

**Invariant**
> 節點會依照 level 或距離由近到遠被處理。

**常見應用**：level order traversal、shortest path (unweighted)、flood fill

---

### 11. Topological Sort

**Invariant**
> 一個節點只能在所有 dependency 都完成後才被處理。

**常見應用**：course schedule、dependency graph

---

### 12. Backtracking

**Invariant**
> 遞迴路徑上的選擇，永遠是一個合法的部分解。

**常見應用**：permutations/combinations、constraint satisfaction

---

### 13. Trie-Based Search

**Invariant**
> Prefix structure 可以提前剪掉不可能的搜尋分支。

**常見應用**：dictionary search、word search 問題

---

### 14. Heap / Priority Queue

**Invariant**
> Heap 的 top 永遠代表目前最優先被處理的候選解。

**常見應用**：top K、streaming median、scheduling

---

### 15. Dynamic Programming

**Invariant**
> 一個狀態的最佳解，只依賴於更小的子狀態。

**常見應用**：optimization、path counting、sequence problems

---

### 16. Bit Manipulation

**Invariant**
> Bitwise operation 可以用來壓縮與操作狀態。

**常見應用**：single number、bit range

---

### 17. Math / Simulation

**Invariant**
> 題目規則是確定的，可以直接依規則模擬或套公式。

**常見應用**：numeric manipulation、matrix simulation、formatting 題

---

### 18. Special / Mixed Patterns

**Invariant**
> 題目依賴特定資料結構或技巧，無法歸納成單一可重用 Pattern。

**Examples**：LRU Cache、Insert Delete GetRandom O(1)、Median of Two Sorted Arrays

---

## 學習策略

### 優先順序（由易到難）

1. **基礎 Pattern**（先掌握）
   - Two Pointers
   - Sliding Window
   - Hashing

2. **進階 Pattern**（需要練習）
   - Binary Search
   - Stack
   - DFS/BFS

3. **困難 Pattern**（需要時間累積）
   - Dynamic Programming
   - Backtracking
   - Topological Sort

### 刻意練習建議

- 每個 Pattern 至少做 5 題
- 先做 Easy 建立信心
- 再做 Medium 熟悉變化
- Hard 題用來檢驗理解深度
- **重點不是背 code，而是理解 invariant**

---