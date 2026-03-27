class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]