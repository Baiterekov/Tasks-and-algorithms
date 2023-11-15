"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

nums = [3,0,1]
miss = 0
nums.sort()
for i in nums:
	if i != miss:
		print(miss)
		break
	miss = miss+1
else: print(miss)
