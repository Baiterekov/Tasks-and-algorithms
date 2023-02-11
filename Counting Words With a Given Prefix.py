"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
"""

words = ["lewsmb","lewrydnve","lewqqm","lewec","lewn","lewb","lewedb"]
pref = "lew"
count = 0
count_pref = 0
for i in words:
	if len(i)<len(pref):
		continue
	for j in range(0, len(pref)):
		if pref[j] == i[j]:
			count = count + 1
		else:
			continue
	if count == len(pref):
		count_pref = count_pref + 1
	count = 0
print(count_pref)
