"""Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned."""

x = int(input("Enter the number: "))
if x==0 or x==1:
    print(x)
else:
    for i in range(0, x+1):
        num = i*i
        print(num)
        if(num==x):
            print(x)
            break
        elif num>x:
            print(i-1)
            break