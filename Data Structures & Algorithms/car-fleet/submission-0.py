class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        index_pos_sorted = sorted(enumerate(position), key= lambda x: x[1], reverse= True)
        print(index_pos_sorted)
        currentFinishTime = 0
        res = 0

        for (i, p) in index_pos_sorted:
            t = (target - p) / (speed[i])
            if t <= currentFinishTime:
                continue
            else:
                res += 1
                currentFinishTime = t
        
        return res

