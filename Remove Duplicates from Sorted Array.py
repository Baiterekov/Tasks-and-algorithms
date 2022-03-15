nums = [0,0,1,1,1,2,2,3,3,4]
expected = []
expected.append(nums[0])
for i in range(1, len(nums)):
	if nums[i-1]!=nums[i]:
		expected.append(nums[i])

print(expected)

