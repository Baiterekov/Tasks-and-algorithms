"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


nums = [0]
j = 0
count = 0

# print(len(nums))

# for i in range(0, len(nums)):
# 	if nums[i]==0:
# 		nums[i]=""
# 		nums.append(0)
# print(nums)
# print(len(nums))

# while True:
# 	print(nums)
# 	if nums[j]=="":
# 		nums.pop(j)
# 		j=j-1
# 	j = j+1
# 	if j==len(nums):
# 		break
# print(nums)

while True:
	if nums[j]==0:
		nums.pop(j)
		j = j-1
		count = count+1
	j= j +1
	if j == len(nums):
		break

for i in range(0, count):
	nums.append(0)

print(nums)