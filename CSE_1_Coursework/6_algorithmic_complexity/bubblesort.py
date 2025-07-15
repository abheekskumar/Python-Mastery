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

def bubbleSort_WRONG_(L):
    for idx1 in range(0,len(L)):
        for idx2 in range(1,len(L)-idx1): # doesn't make sense, this doesn't compare values next to each
            if L[idx1] > L[idx2]: # compare
                L[idx1],L[idx2] = L[idx2],L[idx1] # swap

    return L
def bubbleSort1(L):
    for idx1 in range(0,len(L)):
        for idx2 in range(idx1+1,len(L)): # for each ele, compare the next one till the end
            # if any of them are smaller than the current element, swap them
            # stops at len(L), the range doesn't produce any values in that case
            # print(L)
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
    swap = False
    while not swap: # loop to stop when done O(len(L))
        swap = True # assume no swap this iteration
        for ele in range(1,len(L)): # loop to keep track of comparisons O(len(L))
            print(L)
            if L[ele-1] > L[ele]: # compare
                # swap
                swap = True
                L[ele-1],L[ele] = L[ele], L[ele-1]

    return L

L = [636,23,523,975,33,62,34,626,63]
# print(bubbleSort1(L))
print(bubbleSort2(L))