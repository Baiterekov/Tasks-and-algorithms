import random

unsorted_array = [random.randint(1, 100) for i in range(10) ]		# Created array with size 10 and filled with random number in range 1 to 100
number = 0															# Just variable to change places of number in array

print("unsorted array: ", unsorted_array)							# Shows unsorted array

for j in range(0, 10):												# First loop for sorting array
	for k in range(0, 10): 											# Second loop for sorting array	
		if( unsorted_array[j] < unsorted_array[k]):					# If number in place j in array less than number in place k
			number = unsorted_array[k]								# The program changes their places
			unsorted_array[k] = unsorted_array[j]
			unsorted_array[j] = number
			
print("sorted array: ", unsorted_array)								# Final sorted array