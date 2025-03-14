class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # First pass: Find all the rwos and columns that need to be zeroed
        for i in range(rows):
            for j in range(cols): 
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: Zero out the rows
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0
        # Third pass: Zero out the columns
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0