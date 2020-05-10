def BubbleSort(a):
    
    # sorting smallest to largest order
    sort = False

    while not sort:
        # assume that the array is sorted
        sort = True

        for i in range(1,len(a)):
            curr = a[i]
            prev = a[i-1]

            if prev > curr:
                a[i], a[i-1] = a[i-1], a[i]
                # since we had to sort, set sort variable to false
                sort = False
    return a
