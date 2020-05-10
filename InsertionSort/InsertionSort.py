def InsertionSort(a):
		
	for i in range(1, len(a)):
	    curr = a[i]
	    j = i-1
	    while j >= 0 and a[j] > curr:
		a[j+1] = a[j]
		j -= 1
	    a[j+1] = curr

	return a
