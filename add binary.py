"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
# a = input("Enter binary number: ")
# b = input("Second number: ")
# a=a[::-1]
# b=b[::-1]
# count = 0
# number_a = 0
# number_b = 0
# result_sum = ""
# for i in a:
#     if i=="1":
#         number_a = number_a + 2**count
#     count = count +1
# print(number_a)
# count = 0
# for i in b:
#     if i=="1":
#         number_b = number_b + 2**count
#     count = count +1
# count = 0
# print(number_b)
# number_a = number_a+number_b
# print("sum ", number_a)
# for i in range(0, number_a):
#     if number_a==0 : print(number_a, " 3"); break
#     if number_a==1: result_sum = result_sum+"1"; break
#     else:
#         digit=str(number_a%2)
#         number_a = int(number_a/2)
#         result_sum=result_sum+digit
#     count = count + 1     
#     print(number_a, count, digit)
# result_sum=result_sum[::-1]
# print(result_sum)

a = input("First binary digits : ")
b = input("Second binary digits : ")
 
a = int(a, 2)
b = int(b, 2)

sum = a+b 

sum = bin(sum)

sum = str(sum)

arr = []

digit = ""
for i in sum:
    arr.append(i)
    
for i in range(2, len(arr)):
    digit = digit+arr[i]
print(digit)