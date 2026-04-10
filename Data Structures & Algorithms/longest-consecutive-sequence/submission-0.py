class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = dict()
        maximum = 0
        for i in nums:
            if i in dic:
                continue
            else:
                if not (((i - 1) in dic) or ((i + 1) in dic)):
                    dic[i] = [1, i, i]
                    target = i
                elif ((i - 1) in dic) and ((i + 1) in dic):
                    dic[i - 1][0] = dic[i - 1][0] + 1 + dic[i + 1][0]
                    dic[i - 1][2] = dic[i + 1][2]
                    dic[i] = dic[i - 1]
                    dic[dic[i -1][2]] = dic[i - 1]
                    target = dic[i -1][1]
                elif (i - 1) in dic:
                    dic[i -1][0] += 1
                    dic[i -1][2] = i
                    dic[i] = dic[i -1]
                    target = dic[i - 1][1]
                else:
                    dic[i] = dic[i + 1]
                    dic[i][0] += 1
                    dic[i][1] = i
                    target = i
            maximum = max(maximum, dic[target][0])
        return maximum