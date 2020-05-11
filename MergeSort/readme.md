# Implementation
- divide up the list into 2 recursively, until the list has 1 elements
From the division with smallest number of elements per leaf (i.e. 1 element per leaf)
- recursively merge according to the corrected order, comparing L and R leaves

# time complexity
- worst: $n*log(n)$
- best: $n*log(n)$

# space complexity
- $n*log(n)$
