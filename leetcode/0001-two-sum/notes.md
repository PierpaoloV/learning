# Notes — Two Sum

## My Approach
<!-- Fill in after solving -->
It was a lot of time i wasn't actively coding to solve these basic things. Seemed quite difficult at first but then once solved felt really easy.

## Complexity
- Time: O(?) ??
- Space: O(?) ??

## What I learned
<!-- Fill in after grader review -->
A nicer implementation vould be the following:
```python
def two_sum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
```
Because with a dictionary num_to_index used this way, I kinda remember past iterations, meaning the search would be faster.
