from typing import List
"""
Insertion sort is a sorting algorithm that builds the sorted list
one element at a time from an unsorted list.
it checks each element(from the unsorted list) one by one to the sorted list and 
inserts where necessary

Questions:
why the i in range(1,len(array))?
    the first element is already "sorted". we start looking from the second element onwards
why the j= i-1:
    keeps track of the previous element before key
why the j >= 0 and array[j]>key:
    the while loop is used to move all the elements until you find where the key fits
    the condition has 2 parts: the first one ensure that you go till you hit the first element,
    the second part(plays a bigger role) ensure that you check whether the current j-check(in the sorted subarray) is
    greater than the key.
    If yes(while loop body): move current element to the right and reduce j to check one more element behind
    if no( while loop else clause): you found the perfect place to insert the element- insert it into the right place.

Number of operations:


"""
def insertion_sort_one(unsorted_array) -> list:

    """
    This is my first implementation of insertion sort.
    """
    sorted_array = [] # empty list

    for un_idx in range(0,len(unsorted_array)): # goes over each element
        key = unsorted_array[un_idx]

        # first element adding:
        if len(sorted_array) == 0:
            sorted_array.append(key)
            continue # move onto the next element

        for idx2 in range(0,len(sorted_array)):
            """
            print("Debugging statements:")
            print(idx2)
            print(sorted_array)
            print(key)
            print("*"*50)
            """
            
            if key < sorted_array[idx2]: # ele at curr index is bigger; add it at this index
                sorted_array.insert(idx2,key)
                break # stop checking where we need to insert, we've already found it; check the next key

            if idx2 == len(sorted_array)-1: # if this is the last check, this element is bigger; this is a base case
                # than any of the element in the list, add it to the end of sorted array.
                sorted_array.append(key)
            # if it isn't, the iterator will just skip to the next index

    return sorted_array
ar = [2,6,1,6,34,2345,72,43,673,32]
# print(insertion_sort_one(ar))
def insertion_sort_tb(ar) -> list:
    """
    Textbook implementation of insertion sort.
    """
    array = list(ar)
    for i in range(1,len(array)): # we start from the 2nd element till the end
        key = array[i]
        j = i-1 # j is used to keep track of the element just before key
        while (j >= 0 and array[j]>key): # the (array[j]> key) checks whether the previous element is greater than the 
            # current element(key); if so, move all the elements to the right, until you hit the point where key
            # isn't greater than the previous element OR you hit the beginning of the array. 
            # in that case, you would move into else clause and then just add the key.
            array[j+1] = array[j] # shifting elements to the right to make room for the key
            j = j-1
        else:
            array[j+1] = key # adding the key

    return array
# ar = [2,6,1,6,34,2345,72,43,673,32]
# print(insertion_sort_one(ar))
print(insertion_sort_tb(ar))

from typing import List 


def insertionSort(arr:List[int])->list:
    """ Returns a copy of arr that is sorted using insertion sort."""
    
    for idx1 in range(1,len(arr)): # starts from 1 because 1st element is already sorted in the subarray
        key = arr[idx1]
        idx2 = idx1-1

        while((idx2 >=0) and (arr[idx2] > key)): # loop used to shift elements NOTE: ensure that idx2>=0 condition is checked first
            arr[idx2+1] = arr[idx2] # shifting elements to the right
            idx2 -= 1
        # when 1st element or key is bigger than the element in the subarray, we've found the appropriate spot
        arr[idx2+1] = key # add key to subarray, idx2+1 is used since we've subtracted it on the last iteration in the loop
            # note: the idx2+1 spot is kept at the spot that is non-essential, and can be written over
            # what that means is that we've made a copy of that element before hand
    return arr

# leetcode implementation:

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            # Shift elements of nums[0..i-1], that are greater than key
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key
        
        return nums

                

