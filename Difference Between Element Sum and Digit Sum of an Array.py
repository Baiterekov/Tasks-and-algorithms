"""
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

 

Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation:
The element sum of nums is 1 + 2 + 3 + 4 = 10.
The digit sum of nums is 1 + 2 + 3 + 4 = 10.
The absolute difference between the element sum and digit sum is |10 - 10| = 0.
 

Constraints:

1 <= nums.length <= 2000
1 <= nums[i] <= 2000
"""

nums = [1,15,6,3]
sum_of_elements = 0
sum_of_digits = 0
for i in nums:
	
	sum_of_elements = sum_of_elements + i
	if i > 9:
		for j in str(i):
			sum_of_digits = int(j)+sum_of_digits
	else:
		sum_of_digits = sum_of_digits + i
print(sum_of_elements - sum_of_digits)