class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        counters = []
        for i in strs:
            counter = collections.Counter(i)
            check = False
            for j in range(len(counters)):
                if counter == counters[j]:
                    result[j].append(i)
                    check = True
                    break
            if check == False:        
                counters.append(counter)
                result.append([i])
        return result