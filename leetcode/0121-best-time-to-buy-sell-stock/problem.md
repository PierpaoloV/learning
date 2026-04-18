# 0121 — Best Time to Buy and Sell Stock

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
**Difficulty:** Easy  
**Topics:** Sliding Window, Array  
**Week:** 4

## Problem
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You want to maximize your profit by choosing a single day to buy and a single day to sell **after** the buy day.

Return the maximum profit. If no profit is possible, return `0`.

## Examples
```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5  (buy day 2 at 1, sell day 5 at 6)

Input:  prices = [7, 6, 4, 3, 1]
Output: 0  (prices only fall, no profit possible)
```

## Constraints
- 1 ≤ prices.length ≤ 10⁵
- 0 ≤ prices[i] ≤ 10⁴
