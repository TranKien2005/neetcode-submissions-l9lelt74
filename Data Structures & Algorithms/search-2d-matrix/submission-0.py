class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_size = len(matrix)
        c_size = len(matrix[0])
        l, r = 0, (r_size * c_size - 1)
        
        while l <= r:
            mid = (l + r + 1) // 2
            r_index = mid // c_size
            c_index = mid % c_size
            if (matrix[r_index][c_index] == target):
                return True
            elif (matrix[r_index][c_index] > target):
                r = mid -1
            else:
                l = mid + 1
        
        return False