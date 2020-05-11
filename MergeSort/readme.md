# Implementation
- divide up the list into 2 recursively, until the list has 1 elements
From the division with smallest number of elements per leaf (i.e. 1 element per leaf)
- recursively merge according to the corrected order, comparing L and R leaves

# Time complexity
- worst: $n*log(n)$
- best: n, since you would not have to do merges, which is (log n)

# Space complexity
- n, since the list is stored somewhere at each iteration
