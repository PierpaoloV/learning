# 0020 — Valid Parentheses

**Link:** https://leetcode.com/problems/valid-parentheses/  
**Difficulty:** Easy  
**Topics:** Stack, String  
**Week:** 3

## Problem
Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets
- Open brackets are closed in the correct order
- Every close bracket has a corresponding open bracket

## Examples
```
Input:  s = "()"
Output: true

Input:  s = "()[]{}"
Output: true

Input:  s = "(]"
Output: false

Input:  s = "([)]"
Output: false
```

## Constraints
- 1 ≤ s.length ≤ 10⁴
- s consists of brackets only
