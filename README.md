# LeetCode Patterns – Top Interview 150

這個 repository 以 **解題 Pattern（題型分類 + 解題技巧）** 為核心，系統化整理 LeetCode Top Interview 150。

## 核心目標

> **熟練少數幾個 Pattern 與其 invariant，就能無痛解完 LeetCode Top Interview 150。**

📍 **建議從這裡開始**
- Pattern 與 invariant 總覽 → `00_Overview/Patterns_Overview.md`
- Top Interview 150 題目對照表 → `00_Overview/Top_Interview_150_Map.md`

---

## 為什麼做這個 Repo？

多數人在面試時卡關，不是因為不會寫 code，而是因為**一開始就用錯 Pattern 在思考**。

這個 repo 專注三件事：
- **Pattern 辨識**：看到題目先分類
- **正確的心智模型**：避免直覺誤判
- **以 invariant 為核心的解題決策**

---

## Repository 結構

```
.
├── 00_Overview
│   ├── Patterns_Overview.md
│   └── Top_Interview_150_Map.md
│
├── 01_Two_Pointers
│   ├── lectures
│   ├── problems
│   └── solutions
│
├── 02_Sliding_Window
│   ├── lectures
│   ├── problems
│   └── solutions
│
├── 03_Binary_Search
│   ├── lectures
│   ├── problems
│   └── solutions
│
├── LICENSE
└── README.md
```

---

## 每個 Pattern 包含什麼？

每個 Pattern 資料夾遵守相同結構：

### lectures/
系統化說明這個 Pattern 的解法
- 核心 invariant
- 何時使用
- 思考流程
- 常見模板
- 常見錯誤

### problems/
完整解題筆記（UMPIRE 框架）
- **U**nderstand（理解題意）
- **M**atch（對應 Pattern）
- **P**lan（解題規劃）
- **I**mplement（實作）
- **R**eview（複雜度分析）
- **E**valuate（邊界測試）

### solutions/
參考實作（Python / C++ / Java）

---

## 建議學習方式

### 適合對象
- 即將要面試科技業的轉職生
- 想系統化學習 LeetCode 的大學生
- 需要快速建立解題框架的工程師

### 學習步驟
1. **一次只專注一個 Pattern**
2. **先讀 lecture，記住 invariant**
3. **解 problems 時，強迫自己先判斷 Pattern**
4. **當決策流程變得機械化，再進下一個 Pattern**

### 時間規劃（30 天循環學習計畫）
- Week 1：Two Pointers、Sliding Window、Hashing
- Week 2：Binary Search、Stack、Greedy
- Week 3：DFS/BFS、Linked List、Prefix Sum
- Week 4：DP、Backtracking、複習
- Week 5–8（進階循環）
  - 重刷 Top Interview 150
  - 強化混合 Pattern 題
  - 訓練「10 秒內判斷 Pattern」

---


## 更新節奏

- 每週新增一個 Pattern lecture
- 同步補齊前一個 Pattern 的 problems 與 solutions
- 優先完成 Top Interview 150 高頻題型

---


## 授權

MIT License

---

## 結語

這個 repo 的目標不是刷完題目數量，而是建立一套**可重複使用、可遷移的解題系統**。

如果你覺得這套整理方式對你有幫助，歡迎給一顆 ⭐

---

## 相關資源

- [LeetCode Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Grind 75](https://www.techinterviewhandbook.org/grind75)

---