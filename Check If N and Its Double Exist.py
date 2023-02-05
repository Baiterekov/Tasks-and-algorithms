"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 
"""
arr = [7,1,14,11]
first_condition = 0
second_condition = 0
third_condition = 0
for i in range(0, len(arr)-1):
	for j in range(i+1, len(arr)):	
		if i!=j and 0 <= i and 0<= j:
			first_condition = first_condition+1
		if j< len(arr) and i< len(arr):
			second_condition = second_condition+1
		if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
			third_condition = third_condition+1
# print(first_condition)

# print(second_condition)

# print(third_condition)
	
if third_condition>=1 and second_condition>=1 and first_condition>=1 :
	print(True)
else:
	print(False)


 
