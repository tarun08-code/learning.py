class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in hashmap:
                return [hashmap[needed], i]

            hashmap[num] = i