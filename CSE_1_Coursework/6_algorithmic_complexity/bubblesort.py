"""
Bubble sort:
idea: compare each element of the list with every other, other than the already settled ones.

pseudocode:
for idx in range(0,len(list)): # we iterate over idx(not the element) to to stop the checking
    for idx2 in range(1,len(list)-i) # 1 for every next element
        if list[idx1] > list[idx2]:
            #swap

return list


O(n(n-1)) = O(n^2)
"""

def bubbleSort(L):
    for idx1 in range(0,len(L)):
        for idx2 in range(1,len(L)-idx1):
            if L[idx2-1] > L[idx2]: # compare
                L[idx2-1],L[idx2] = L[idx2],L[idx2-1] # swap
    return L

ar = [2,6,1,6,34,2345,72,43,673,32]
# print(bubbleSort(ar))


def bubbleSort1(L): # this is not bubble sort, it's something else
    """This implementation sorts the list from the beginning."""
    for idx1 in range(0,len(L)):
        for idx2 in range(idx1+1,len(L)): # for each ele, compare the next one till the end
            # if any of them are smaller than the current element, swap them
            # stops at len(L), the range doesn't produce any values in that case
            if L[idx1] > L[idx2]: # compare
                L[idx1],L[idx2] = L[idx2],L[idx1] # swap
    return L
"""
Course Bubble sort implementation
- compare consequtive pairs of elements
- swap elements in pairs such that the smaller is first
- when you reach the end of the list, start over
- stop when no more swaps have been made

- this leads to the back of the list being completely sorted first, and then it moves to the front


Implementation:
- keep a flaged while loop to see whether or not there
    were any comparisons this time iterating through the loop.
- stage flag to positive case(end the loop)
- an inner loop to go through all the elements and compare.
- if a swap is needed, reset flag( continue the loop)


O(n^2)
"""

def bubbleSort2(L):
    swap = True # assume swap needs to happen to start loop
    while swap: # loop to stop when done O(len(L))
        swap = False # assume no swap this iteration
        for ele in range(0,len(L)-1): # loop to keep track of comparisons O(len(L))
            if L[ele] > L[ele+1]: # compare
                # swap
                swap = True
                L[ele],L[ele+1] = L[ele+1], L[ele]
    return L

print(bubbleSort1(ar))
print(bubbleSort2(ar))

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                # print(L)

    print("Final L: ", L)
    
# L = [636,23,523,975,33,62,34,626,63]
# print(modSwapSort(L))
    