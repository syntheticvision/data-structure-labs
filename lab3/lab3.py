#
# Author: Babak Ghafourigivi
# Student Number: 165118233
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)


def linear_search(list, key):
	def search_recursive(list, key, index):
		if index == len(list):
			return -1
		if list[index] == key:
			return index
		return search_recursive(list, key, index + 1)

	return search_recursive(list, key, 0)


def binary_search(list, key):
	def search_recursive(list, key, low, high):
		if low > high:
			return -1
		mid = (low + high) // 2
		if list[mid] == key:
			return mid
		elif key < list[mid]:
			return search_recursive(list, key, low, mid - 1)
		else:
			return search_recursive(list, key, mid + 1, high)

	return search_recursive(list, key, 0, len(list) - 1)
