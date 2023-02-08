"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

s = "Let's take LeetCode contest"
arr = s.split(" ")
reverse = ""
reverse_arr = []
for i in arr:
	for j in i:
		reverse = j+reverse
	reverse_arr.append(reverse)
	reverse = ""	
for k in reverse_arr:
	reverse = reverse + k + " "


print(reverse[:-1])

