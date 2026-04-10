class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = list(collections.Counter(nums).items())
        counter = sorted(counter, key=lambda x: -x[1])
        print(counter)
        return [x[0] for x in counter[:k]]
