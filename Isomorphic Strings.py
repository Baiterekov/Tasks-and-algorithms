"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


s= "badc"
t = "asfg"
word1 = ""
word2 = ""

dict1 = {}
dict2 = {}

if len(s)!=len(t):
	print(False)
else:
	for i in range(0, len(s)):
		dict1[s[i]]=t[i]
		dict2[t[i]]=s[i]

	for i in range(0, len(s)):
		word1 = word1 + dict1[s[i]]
		word2 = word2 + dict2[t[i]]

	if word1==t and word2 == s:
		print(True)
	else:
		print(False)
