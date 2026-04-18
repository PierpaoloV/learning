# Notes — Two Sum

## Approach
Hash map: store each number's index as we iterate. For each element, check if its complement (`target - n`) is already in the map.

## Complexity
- Time: O(n) — single pass
- Space: O(n) — hash map

## Common mistakes
- Brute force O(n²) nested loop works but won't pass at scale
- Don't return the values — return the **indices**
- Same element can't be used twice, but duplicate values are OK (e.g. [3,3], target=6)
