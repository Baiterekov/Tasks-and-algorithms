"""Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""

import re
s = "ab_a"

word = re.split(r"[\b\W\b]+|[-*/+!@#?$()%^&*_\,.:;''\[\] \"{}]", s.lower())
# word = re.split("[-*/+!@#?$()%^&*_\,.:;''\[\] \"{}]", s.lower())
# word = re.split(r"\s(?=[A-Z])|[-*/+!@#?$()%^&*_\,.:;''\[\] \"{}]", s.lower())

word2 = ""
for i in word:
    word2 = word2 + i
palindorme = word2[::-1]
print(word2)
print(palindorme)
if palindorme==word2:
    print(True)
else:
    print(False)
