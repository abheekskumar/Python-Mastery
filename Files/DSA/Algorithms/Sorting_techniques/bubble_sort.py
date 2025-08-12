from typing import List
"""
Bubble sort: General idea is to compare adjacent elements and exchange them if the first one is
bigger than the second one.

algorithm:
for i in lower to upper:
    for j in lower to (upper -1 -i):
        if ar[j] > ar[j+1]:
            # swap them
            ar[j], ar[j+1] = ar[j+1], ar[j]
            or
            temp = ar[j]
            ar[j] = ar[j+1]
            ar[j+1] = temp

The first for loop iterates over each element
the second for loop iterates allows us to check each element to every other one
except the one that it just finished moving.

So the way this works is that initially, we would have an unsorted array, then 
we would have the last element in the right place, the then last but one.

the general idea of Bubble sort leads to putting the heaviest element in the last place constantly.
the first iterator allows us to see each element, the second iterator goes from the beginning to the "heaviest" element
that bubble sort has been through


why is the range for the second loop from 0 to upper-1-element:
    the 0 compares from the begining
    the upper-1-element ensures that we don't compare it to the heavier elements we've already
    settled.

    
Number of operations:

in terms of comparisons:
for the first pass, we compare it with everything but itself(n-1) comparisons
for the second pass, we compare ti with everythin but itself and what we've just set(n-2) comparisons
therefore: for n elements, we have time complexity of n^2
based on the number of swappings that occur, we also have time complexity of n^2.

total in the worst case = 2n^2


"""

def bubble_sort(ar) -> list:
    """
    Returns a sorted array(list) using bubble sort.
    """
    ar2 = list(ar)
    for ele in range(0,len(ar2)): # goes over each element
        for ele2 in range(0,len(ar2)-1-ele): # gives scope for checking each element with everything ahead of it in the array
            if ar2[ele2] > ar2[ele2+1]: # compares each element
                #swap them
                ar2[ele2],ar2[ele2+1] = ar2[ele2+1], ar2[ele2]
    return ar2

ar = [2,6,1,6,34,2345,72,43,673,32]
print(bubble_sort(ar))




def bubbleSort2(ar:list) -> None:
    """Sorts the array in place using bubble sort"""
    for idx1 in range(len(ar)):
        swapped = False
        for idx2 in range(len(ar)-idx1-1):# -idx1 ensures we don't check the last subarray that is sorted
            # the -1 ensure that we can do [idx2+1] to check pairs of elements safely.
            if ar[idx2] > ar[idx2+1]:
                ar[idx2], ar[idx2+1] = ar[idx2+1] , ar[idx2]
                swapped = True
        if not swapped: # optimization to stop comparisons if no elements were swapped in one iteration
            break

ar = [2,6,1,6,34,2345,72,43,673,32]
bubbleSort2(ar)
print(ar)

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
    

# Leetcode implementation:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break  # Early exit if already sorted
        return nums