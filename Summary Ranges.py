"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

# nums = [0,2,3,4,5,7,9,10,11,12,14]
nums = []
range_sum = []
i = 1
j = 0
if len(nums)==0:
	print(nums)
else:
	first_elm = nums[0]
	last_elm = 0
	count = 0
	while True:
		if i == len(nums):
			last_elm = nums[j]
			if nums[j]!=nums[j-1]+1:
				range_sum.append(str(last_elm))
			else:
				range_sum.append(str(first_elm)+"->"+str(last_elm))

			break

		if nums[i] == nums[j]+1:
			count = count+1
		else:
			
			if count == 0:
				range_sum.append(str(first_elm))
				
			else:
				last_elm = nums[j]
				range_sum.append(str(first_elm)+"->"+str(last_elm))
				
			first_elm = nums[i]
			count = 0
		
		i = i+1
		j = j+1



	print(range_sum)
