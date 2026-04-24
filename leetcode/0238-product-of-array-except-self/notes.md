# Notes — Product of Array Except Self

## My Approach
It was not easy to solve this question. The core idea is to calculate the product of the elements to the left of the current element and the product of the elements to the right of the current element. Then multiply these two products together to get the final result.
I used three arrays to store the prefix products, suffix products, and the final solutions.

## Complexity
- Time: O(n)
- Space: O(n)

## What I learned
Back when i was in uni i would be so able to solve this problem in 5 minutes. Now it feels like with built in libraries i stopped thinking.
