"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false
 

Constraints:

coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
"""

height = ["a", "b", "c", "d", "e", "f", "g", "h"]
width = ["1", "2", "3", "4", "5", "6", "7", "8"]
dict_board = {}
count = 1
coordinates = "c7"
for i in range(0, len(height)):
	for j in range(0,len(width)):
		if count%2 == 0:
			dict_board[height[i]+width[j]] = True
		else:
			dict_board[height[i]+width[j]] = False
		count = count + 1
	count = count - 1

print(dict_board[coordinates])


print(dict_board)