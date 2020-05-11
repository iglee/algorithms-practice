def MergeSort(a):
    if len(a) > 1:
        m = len(a) // 2
        L = a[:m]
        R = a[m:]
        
        MergeSort(L)
        MergeSort(R)
        print("L = ", L)
        print("R = ", R)
        print(a)
        
        #initialize index:
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k+=1
        print("post merge")
        print("L = ", L)
        print("R = ", R)
        print(a)
        print("\n\n")
        print(i)
        print(j)
        print(k)
        print("\n\n")
        
        # if there are remaining elements due to the other list index reaching the length
        if j == len(R):
            a[k] = L[i]
        elif i == len(L):
            a[k] = R[j]
    return a
