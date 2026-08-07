class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        x=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                x.append(matrix[i][j])
        x.sort()
        return x[k-1]