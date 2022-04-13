"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

numRows = 5
sum_n = 0

m=1
A = [] 
for i in range(numRows): 
    A.append([1] * m)
    m=m+1

for i in range(2, numRows):
	for j in range(1,len(A[i])-1):
		sum_n = A[i-1][j-1]+A[i-1][j]
		A[i][j]=sum_n

print(A)