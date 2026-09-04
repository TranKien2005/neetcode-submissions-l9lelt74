class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counter = list(counter.items())
        counter = sorted(counter, key= lambda x: x[1], reverse= True)
        return [item[0] for item in counter[0:k]]