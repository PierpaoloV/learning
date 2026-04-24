from typing import List
import numpy as np


def contains_duplicate(nums: List[int]) -> bool:
    unique_nums = np.unique(nums) # remove duplicates #here is true if there are no duplicates, we want to return false in that case
    return not (len(unique_nums) == len(nums))
