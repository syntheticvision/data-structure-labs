# Analysis and Reflection for Lab 3

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):   # 1
		return 1        # 1
	elif (number == 1): # 1
		return value    # 1
	else:
		return value * function1(value, number-1) # 2n
```
Tn = 2n + 4 => T(n) is O(n)

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):            # 1
		return True         # 1
	else:
		if(mystring[a] != mystring[b]): # 1
			return False                # 1
		else:
			return recursive_function2(mystring,a+1,b-1)    # 2 + (n-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1) # 2 * n/2

```
Tn = 6 + n - 1 + n => 2n + 5 so T(n) is O(n)

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):                       # 1
		return 1                            # 1
	elif (number == 1):                     # 1
		return value                        # 1
	else:
		half = number // 2                  # 2
		result = function3(value, half)     # 1 + n/2
		if (number % 2 == 0):               # 1
			return result * result          # 2
		else:
			return value * result * result  # 3

```
for even number T(n) = n/2 + O(1) or for odd number T(n) = n/2 + O(1)

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?
When I approach writing recursive functions, I start by thinking about the base case first. That's the simplest version of the problem that can be solved directly, 
like returning 1 for a factorial of 0. Then, I figure out how to break the problem into smaller parts so that each call to the function gets closer to the base case. Finally, I make sure each recursive call works towards that goal and that the logic for combining the results is sound.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 
For analyzing recursive functions, I break it down by looking at how many times the function calls itself. It's different from non-recursive analysis because I need to account for how the input size shrinks with each call (usually halved or reduced by 1).
But in both cases, I still look at the number of operations performed at each step, which stays the same.
