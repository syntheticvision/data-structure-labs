def partb_one(mylist, key):
	total = 0								# 1
	for i in range(len(mylist)):			# 2 + (n-1)
		for j in range(i+1,len(mylist)):    # (n−1)+(n−2)+(n−3)+ ⋯ +1
			if i != j:						# 2
				if mylist[i] + mylist[j] == key: # 2
					total += 1				# 2
	return total							# 1

# Tn = 1 + 2 + (n-1) + (n-1)*n/2 + 2 + 2 + 2 + 1 => n^2-n/2 + (n-1) + 10 => O(n^2)

def partb_two(mylist, key):
	total = 0
	mylist.sort()
	i = 0
	j = len(mylist)-1
	while (i < j):
		if(mylist[i] + mylist[j] < key):
			i+=1
		elif(mylist[i] + mylist[j] > key):
			j-=1
		else:
			total += 1
			i+=1
			j-=1
	return total

# O(n log n)

def partb_three(mylist, key):
	items={}                   		# 1
	total = 0						# 1
	for number in mylist:			# n - 1
		items[number]=1				# 1
	for number in mylist:			# n - 1
		other = key-number			# 2
		if(other in items):			# n - 1
			total+=1				# 2
	return total//2					# 1

# O(n)