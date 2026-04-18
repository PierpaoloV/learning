# 0015 — 3Sum

**Link:** https://leetcode.com/problems/3sum/  
**Difficulty:** Medium  
**Topics:** Two Pointers, Sorting  
**Week:** 3

## Problem
Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets.

## Examples
```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:  nums = [0, 1, 1]
Output: []

Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

## Constraints
- 3 ≤ nums.length ≤ 3000
- -10⁵ ≤ nums[i] ≤ 10⁵
