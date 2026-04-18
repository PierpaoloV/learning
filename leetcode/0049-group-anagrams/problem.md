# 0049 — Group Anagrams

**Link:** https://leetcode.com/problems/group-anagrams/  
**Difficulty:** Medium  
**Topics:** Array, Hash Map, Sorting  
**Week:** 2

## Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Two strings are anagrams if one is a rearrangement of the other's characters.

## Examples
```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input:  strs = [""]
Output: [[""]]
```

## Constraints
- 1 ≤ strs.length ≤ 10⁴
- 0 ≤ strs[i].length ≤ 100
- strs[i] consists of lowercase English letters
