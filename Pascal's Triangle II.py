"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

rowIndex = 3
rowIndex +=1
sum_n = 0

m=1
A = [] 
for i in range(rowIndex): 
    A.append([1] * m)
    m=m+1

for i in range(2, rowIndex):
	for j in range(1,len(A[i])-1):
		sum_n = A[i-1][j-1]+A[i-1][j]
		A[i][j]=sum_n

print(A[-1])