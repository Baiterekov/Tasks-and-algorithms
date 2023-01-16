"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

strs = ["sabc", "sac", "sbc"]
pref = ""
elem = ""
arr_len = []
if len(strs)>1:
	for i in range(0, len(strs)):
		arr_len.append(len(strs[i]))

	for i in range(0, min(arr_len)):
		elem = strs[0][i] 
		for j in range(0, len(strs)):
			if strs[j][i]!=elem:

				break
		if strs[j][i]!=elem:
				
				break
		pref = pref+elem

	if pref == "":
		print("There is no common prefix among the input strings.")


	print(pref)

else: print(strs[0])


