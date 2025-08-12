from typing import List
"""
Selection sort:
Idea:
- find the smallest element
- set it in index 0
- find the next smallest element in the sublist
- set it at index 1
- build the list from the first sorted element to the last(build it from the beginning)

plans:
recursion??

while loop to keep track of the last element

comparison for 1 element with every element
if new ele is bigger, exchange them and continue
when the end of the list is hit, set this at index 0 and start checking for index 1


- sorts elements from the front of the list

"""
sortTest = []
def selectionSort1INCORRECT(L):
    # base case
    global sortTest
    if len(L) == 1: # if only one element is left, just return that
        return L
    # recursive case
    for ele in range(1,len(L)): # loop to check over and find the smallest element
        

        # recursive case hit
        return sortTest + selectionSort1(L[1:]) # all but the first element
        


"""
Course selection sort:
loop invariant:
given the prefix of a list which is the all the elements uptill i, and the suffix from i+1 till the end of the list
the prefix is sorted and the suffix contains no element which is smaller than the ones in the prefix.
L[0:i] - prefix, sorted
L[i+1:len(L)] - suffix, not sorted, each element is equal to or bigger than that of the suffix.

outer loop is is len(L)
inner loop is len(L)-i, which is approximately in len(L)

therefore, O(n^2)

guranteed that the first i elements were sorted
maybe a bit better than bubblesort time wise.
"""

def selectionSort1(L): 
    suffixStart = 0 # starting the suffix
    while suffixStart != len(L):
        for idx in range(suffixStart,len(L)): # for all elements in the suffix
            if L[suffixStart] > L[idx]: # if any of those elements are greater
                L[suffixStart],L[idx] = L[idx],L[suffixStart] # swap
        suffixStart +=1 # start checking from the next element onwards
    return L

L = [636,23,523,975,33,62,34,626,63]
print(selectionSort1(L))

def selectionSort2(arr: List[int]):
    """ More efficient traditional implementation of selection sort."""
    for suffixStart in range(0,len(arr)):
        minIndex = suffixStart 
        for idx in range(suffixStart +1, len(arr)): # loop to find min index
            if arr[minIndex] > arr[idx]:
                minIndex = idx
        arr[suffixStart], arr[minIndex] = arr[minIndex], arr[suffixStart] # always suffix start to minIndex value

L = [636,23,523,975,33,62,34,626,63]
selectionSort2(L)
print(L)

# leetcode implementation:

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minIndex = i
            for j in range(i + 1, n):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums