class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        int r_current = 0;
        int c_current = columns - 1;

        while ((r_current < rows) && (c_current) >= 0) {
            if (matrix[r_current][c_current] == target) {
                return true;
            }
            else if (matrix[r_current][c_current] > target) {
                c_current -= 1;
            }
            else {
                r_current += 1;
            }
        }
        return false;
    }
}
