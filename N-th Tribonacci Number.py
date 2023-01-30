"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
n = 5
T2 = 1
T1 = 0
T3 = 1
T = 0

if n == 0:
	print(T1)
if n==1 or n==2:
	print(T2)
else:

	for i in range(0, n-2):
		T = T1 + T2+ T3
		T1 = T2
		T2 = T3
		T3 = T

	print(T)
