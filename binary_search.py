#!/usr/bin/python3 

# importing modules 
import os  
import sys 
import time 

def intro(): 
	os.system('cls') # clearing the screen 
	print('- Binary Search Algorithm -') 	

def algorithm(): 
	data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # list of numbers 
	print(data) # outputing the data to the user 
	target = input('Target: ') # user picks a target to find 
	target = int(target)
	# prompting user for input if the target is not in the list 
	while target not in data:  
		target = input('Target: ')
	start_point = 0 # start point in the data list 
	end_point = len(data) - 1 # end point in the data list 
	# ---- MAIN LOGIC ---- 
	while start_point <= end_point:
		middle = start_point + (end_point - start_point) // 2 # finding the middle point 
		middle_value = data[middle]  # middle value 
		# printing the target and index if the algorithm finds the target 
		if middle_value == target: 
			os.system('cls') # clearing the screen 
			print('---------')
			print('Target: ' + str(target))
			print('---------')
			print('Index: ' + str(middle_value))
			print('---------')
			sys.exit() 
		elif target < middle_value:
			end_point = middle - 1 # changing the end point if the target is lower than the middle value 
		else: 
			start_point = middle + 1  # changing the start point if the target is higher than the middle value 
	print('Target not found!') 


def main(): 
	intro() # calling the intro function 
	algorithm() # calling the algorithm function 

# calling the main function as soon as the program starts 
if __name__ == '__main__': 
	main() # main function is called 