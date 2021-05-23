# efficient list counting
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        '''
        Return the k most frequent ints
        input: list[int],[int]
        output: list
        >>> topKFrequent([1,1,1,2,2,3], k=2)
        >>> [1,2]
        '''
        # utilize Counter.most_common(k) and grab the key-value
        return [i[0] for i in Counter(nums).most_common(k)]