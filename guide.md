# Learning Guide

## Weekly Schedule (3–5 hours/week)

| Day | Activity | Time |
|---|---|---|
| Mon | LeetCode problem | 40 min |
| Wed | LeetCode problem | 40 min |
| Thu | Flashcard review | 60 min |
| Fri | LeetCode problem | 40 min |
| Sat | System design | 60 min |

---

## Step 1 — Do a LeetCode Problem (Mon / Wed / Fri)

1. Open the next problem folder in `leetcode/` (e.g. `0001-two-sum/`)
2. Read `problem.md`
3. Open `solution.py` — delete the placeholder and write your own solution
4. Run the tests:
   ```
   cd ~/projects/personal/learning
   pytest leetcode/0001-two-sum -v
   ```
5. Write your approach and complexity analysis in `notes.md`
6. Run the grader:
   ```
   cd ~/projects/personal/learning
   OPENAI_API_KEY=sk-... python grader/grade.py leetcode/0001-two-sum
   ```
7. Read the `review.md` that appears — fix anything flagged

---

## Step 2 — Flashcard Review (Thu)

1. Open terminal, go to `~/projects/personal/learning/`
2. Run:
   ```
   python ml-fundamentals/review.py
   ```
3. Read the front of the card → press Enter → read the answer → rate yourself:
   - **0** — complete blackout
   - **3** — correct but needed effort
   - **5** — perfect recall
4. The app schedules each card automatically (harder cards come back sooner)

---

## Step 3 — System Design (Sat)

1. Go to `system-design/`
2. Create a folder for the topic (e.g. `url-shortener/`)
3. Write your design in `design.md`:
   - What are the requirements?
   - High-level architecture (components, APIs)
   - Database choice and schema
   - How does it scale?
   - What are the bottlenecks?
4. Run the grader:
   ```
   OPENAI_API_KEY=sk-... python grader/grade.py system-design/url-shortener
   ```
5. Read `review.md` — study the gaps

---

## Step 4 — Update the Weekly Log (end of week)

Open `log.md` and add:

```
## Week of YYYY-MM-DD
Hours: X
LeetCode: [problem names + scores /25]
Flashcards: [how many reviewed, weakest card]
System design: [topic + score /30]
Notes: [anything surprising, patterns noticed]
```

---

## Step 5 — Push to GitHub

```
cd ~/projects/personal/learning
git add -A
git commit -m "week YYYY-MM-DD"
git push
```

---

## LeetCode Order (Blind 75)

Work through these in order — each topic builds on the previous:

### Arrays & Hashing
- [x] 0001-two-sum
- [x] 0049-group-anagrams
- [x] 0217-contains-duplicate
- [x] 0238-product-of-array-except-self
- [ ] 0271-encode-decode-strings

### Two Pointers
- [ ] 0125-valid-palindrome
- [ ] 0167-two-sum-ii
- [ ] 0015-3sum
- [ ] 0011-container-with-most-water

### Sliding Window
- [ ] 0121-best-time-to-buy-sell-stock
- [ ] 0003-longest-substring-without-repeating
- [ ] 0424-longest-repeating-char-replacement
- [ ] 0076-minimum-window-substring

### Stack
- [ ] 0020-valid-parentheses
- [ ] 0155-min-stack
- [ ] 0150-evaluate-reverse-polish-notation

### Binary Search
- [ ] 0153-find-minimum-in-rotated-sorted-array
- [ ] 0033-search-in-rotated-sorted-array

### Linked List
- [ ] 0206-reverse-linked-list
- [ ] 0021-merge-two-sorted-lists
- [ ] 0143-reorder-list
- [ ] 0141-linked-list-cycle

### Trees
- [ ] 0104-maximum-depth-of-binary-tree
- [ ] 0226-invert-binary-tree
- [ ] 0102-binary-tree-level-order-traversal
- [ ] 0235-lowest-common-ancestor-of-bst

### Dynamic Programming
- [ ] 0070-climbing-stairs
- [ ] 0322-coin-change
- [ ] 0300-longest-increasing-subsequence
- [ ] 0072-edit-distance

### Graphs
- [ ] 0200-number-of-islands
- [ ] 0133-clone-graph
- [ ] 0207-course-schedule

---

## System Design Topics (in order)

- [ ] URL shortener (tinyurl)
- [ ] Key-value store
- [ ] Rate limiter
- [ ] News feed / Twitter timeline
- [ ] Notification system
- [ ] Search autocomplete
- [ ] ML feature store
- [ ] ML training platform (like SageMaker)
- [ ] Real-time recommendations system

---

## Flashcard Rating Guide (SM-2)

| Score | Meaning | Next review |
|---|---|---|
| 0 | Complete blackout | Tomorrow |
| 1 | Wrong but remembered on seeing answer | Tomorrow |
| 2 | Wrong but answer was easy | Tomorrow |
| 3 | Correct with significant effort | ~6 days |
| 4 | Correct with minor hesitation | ~10 days |
| 5 | Perfect, instant recall | ~14 days |
