# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;                        # 1

	for i in range(0,number):       # n - 1
		x = (i+1)                   # 2 + n
		total+=(x*x)                # 3n

	return total                    # 1
```
Tn = 1 + n - 1 + 2 + n + 3n + 1 => 5n + 3


### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6  # n * (n + 1) * (n + 2) + 1
```
Tn = n * n^2 + 2n + n + 2 + 1 => n^3 + 3n + 1
Tn is O(n^3)

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):        # n - 1
		for j in range(0,len(list)-1-i):   # (n−1)+(n−2)+(n−3)+ ⋯ +1 
			if(list[j]>list[j+1]):         # 2
				tmp=list[j]                # 1
				list[j]=list[j+1]          # 2
				list[j+1]=tmp              # 2
```
Tn = n-1 + (n-1)*n/2 + 7 => n-1 + n^2-n /2 + 7 
so the inner loop has O(n^2) time complexity while outer loop has O(n) but I'm not sure
if the total time complexity for this function would be O(n^3) or it would be O(n^2). It's a bit hard to understand.

### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1                         # 1
	for i in range(1, number):      # (n-1) + 1
		total=total*(i+1)           # 3 (n-1)
	return total                    # 1 
```
Tn = 1 + (n-1) + 1 + 3n - 3 + 1 => 4n - 1 so Tn is O(n)

## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Babak Ghafourigivi
	* Ashkan Rahimpour

### Timing Data

grab a screenshot of your Excel graphs and put it here

![function 1](https://github.com/user-attachments/assets/e00413e5-fe58-4031-827d-aabad8146ed9)
![function 2](https://github.com/user-attachments/assets/311157da-0926-4162-9c28-37846869454f)
![function 3](https://github.com/user-attachments/assets/f5ee7805-b7ef-4e18-b8bc-e93d87925f9e)



### Summary 
|function| runtime based on analysis | Most similar curve | 
|---|---------------------------|--------------------|
|partb_one()| 684.8284700780059         | Exponential        |
|partb_two()| 0.043740672001149505      | Loglinear          |
|partb_three()| 0.024645436991704628      | Linear             |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

Lab 1 codes to me look cleaner and run faster because of how the approach to solutions are. the more nested loops and complicated solution results in longer run time and harder to read and understand codes

## Reflection:

1. for each function what growth rate best match your results? 
    Function 1: 50000 to 100000      Function 2 and 3 both after 10000
2. Does your analysis match your analysis?  If not, where do you suppose the error occurred?
    I don't understand this question?
3. What sort of conclusions can you draw based on your observations?
    I realized that based on how a function is written, the syntaxes uses and the structure it has to solve a problem affects both the
    readability and run time of a function. for example the first function is quadratic and 
    when I increased the data size just by small increment, the run time would increase by a lot whereas the other two functions would not have such exponential
    growth to their runtime.


