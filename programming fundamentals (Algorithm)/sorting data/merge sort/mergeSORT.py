 # Implement a merge sort with recursion

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
       mid = len(dataset) //2
       leftarr = dataset[:mid]
       rightarr = dataset[mid:]

       # TODO: recursively break down the arrays
       mergesort(leftarr)
       mergesort(rightarr)

       i=0
       j=0
       k=0

       #TODO: while both arrays have content
       while  i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        #TODO: if the left array still has values, add them
       while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        #TODO: if the right array still has values, add them
       while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


#TODO: test the merge sort with data
print(items)
mergesort(items)
print(items)