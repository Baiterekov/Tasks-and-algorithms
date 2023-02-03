"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
Accepted
814K
Submissions
1.4M
Acceptance Rate
56.4%
"""

nums = [1,0,1,1,0,1]
count = 0
max_1 = []


for i in range(0, len(nums)):
	if nums[i] == 0:
		max_1.append(count)
		count = 0
	else:
		count = count+1
if count>0:
	max_1.append(count)
print(max(max_1))