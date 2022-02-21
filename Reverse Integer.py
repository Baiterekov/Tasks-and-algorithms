"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

x = int(input("Enter integer: "))
reverse_integer = ""
if x < 0:
 	x=x*(-1)
 	reverse_integer = "-"
str_x = str(x)

for i in range(0, len(str_x)):
	number = int(x%10)
	str_number = str(number)	
	reverse_integer = reverse_integer+str_number
	x = x/10
reverse_integer = int(reverse_integer)

if reverse_integer>(2**31)-1 or reverse_integer< (-2**31):
	print(0)
else:
	print(reverse_integer)