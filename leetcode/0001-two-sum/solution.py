from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for index1, element1 in enumerate(nums):
        for index2, element2 in enumerate(nums):
            if index1 == index2:
                #same element, skip
                continue
            result = element1 + element2
            if result == target:
                return [index1, index2]
