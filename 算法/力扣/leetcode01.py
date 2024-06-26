# -*- coding: utf-8 -*-

from typing import List


class Solution:

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:

        nums_new = [target - num for num in nums]

        for i in range(len(nums_new)):

            for j in range(i + 1, len(nums_new)):

                if nums_new[i] + nums_new[j] == target:

                    return [i, j]

    @staticmethod
    def twoSum_hash(nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[num] = i
