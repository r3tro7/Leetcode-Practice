class Solution:
	def matSearch(self,mat, N, M, X):
		# Complete this function
		row = 0
		col = M - 1
		while((row < N) and (col >= 0)):
		    if(mat[row][col] == X):
		        return 1
		    elif(mat[row][col] > X):
		        col -= 1
		    else:
		        row += 1
		return 0
