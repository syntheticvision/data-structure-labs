# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Babak Ghafourigivi
# Student Number: 165118233
#

def wins_rock_scissors_paper(player, opponent):
	player = player.lower()
	opponent = opponent.lower()

	if (player == 'rock' and opponent == 'scissors') or \
	   (player == 'paper' and opponent == 'rock') or \
	   (player == 'scissors' and opponent == 'paper'):
		print("player wins")
		return True

	else:
		print("player lost")
		return False


def factorial(n):
	if n < 0:
		return None

	if n == 0:
		return 1

	result = 1
	for i in range(1, n + 1):
		result *= i

	return result


def fibonacci(n):
	if n < 0:
		return None

	if n == 0:
		return 0
	elif n == 1:
		return 1

	prev2 = 0  # F0
	prev1 = 1  # F1
	current = 0

	for i in range(2, n + 1):
		current = prev1 + prev2
		prev2 = prev1
		prev1 = current

	return current


def sum_to_goal(numbers, goal):
	for i in range(len(numbers)):
		for j in range(i + 1, len(numbers)):
			if numbers[i] + numbers[j] == goal:
				return numbers[i] * numbers[j]
	return 0


class UpCounter:
	def __init__(self, step_size=1):
		self.counter = 0
		self.step_size = step_size

	def count(self):
		return self.counter

	def update(self):
		self.counter += self.step_size


class DownCounter(UpCounter):
	def update(self):
		self.counter -= self.step_size
