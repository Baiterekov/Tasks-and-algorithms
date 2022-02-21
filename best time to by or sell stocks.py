"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""

prices = [7, 4, 2, 5, 3]
if len(prices)==1:
    print(0)
max_stock = []
count = 0
for i in range(0, len(prices)):
    count = count+1
    for j in range(count, len(prices)):
        max_stock.append(prices[j]-prices[i])

max_price = max(max_stock)
if max_price<0:
    print(0)
else: print(max_price)


# if not prices:
#         return 0

#     max_prof = 0
#     min_price = prices[0]

#     for i in range(1, len(prices)):
#         if prices[i] < min_price:
#             min_price = prices[i]
#         max_prof = max(max_prof, prices[i] - min_price)
#     return max_prof