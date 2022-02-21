"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""
x = int(input("Enter the number: "))
if(x<0):
	print(bool(0))
array_numbers=[]
reverse = ""
for i in str(x):
	array_numbers.append(i)
for j in reversed(range(len(array_numbers))):
	reverse = reverse + array_numbers[j]
reverse = int(reverse)
if(x==reverse):
	print(bool(1))
else:
	print(bool(0))



