from typing import List
import numpy as np


def product_except_self(nums: List[int]) -> List[int]:
 #given array of n elements, return an array of n elements where the ith element is the 
 # product of all the elements in the original array except the ith element


    solutions = [1] * len(nums)
    suffix_product = [1] * len(nums)
    prefix_product = [1] * len(nums)
    running = 1

    for i in range(len(nums)):
        prefix_product[i] = running
        running *= nums[i]

    running = 1

    for i in range(len(nums) -1, -1, -1):
        suffix_product[i] = running
        running *= nums[i]
    
    for index, number in enumerate(nums):
        solutions[index] = prefix_product[index] * suffix_product[index]
    return solutions

    

