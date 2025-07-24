from typing import List
"""
Merge Sort:
divide and conquer approach:
- if list is of len 1 or 0, it's sorted
- else split into approximately 2 parts and sort each
- merge sorted sublists
    look at the first element in each, move the smaller one into the end of result
    when one list is empty, just copy the rest of the list

Complexity:
at the recursive level:
O(n)

dividing list into half at each recursive level:
O(log(n))


total:
O(nlog(n)) - the fastest a sort can be
"""

def mergeSort(L):
    def mergeSortMerger(L1,L2):
        """ Given 2 sorted lists L1 and L2;returns a resulting list that is sorted."""
        result = []
        i = 0
        j = 0
        while ((i < len(L1)) and (j < len(L2))):
            if L1[i] > L2[j]:
                result.append(L2[j])
                j += 1
            else:
                result.append(L1[i])
                i += 1

        while (i < len(L1)):
            result.append(L1[i])
            i += 1
        while (j < len(L2)):
            result.append(L2[j])
            j += 1

        return result
    def mergeSortRecur(L):
        """ If len(L) > 2, splits into half and recurs. returns the merge list at each cascading level."""

        if len(L) < 2:
            return L[:]
        else:
            half = len(L)//2
            L1 = mergeSortRecur(L[:half])
            L2 = mergeSortRecur(L[half:])
            return mergeSortMerger(L1,L2)
    return mergeSortRecur(L)

def mergeSortReverse(L:list)-> None:
    """ Returns a sorted L using a merge sort algorithm. [in O(nlog(n))]
    """

    def merge(L1,L2):
        """ Returns a sorted merged list L1 and L2"""
        ptr1 = 0
        ptr2 = 0
        res = []
        # until the either of the lists run out of elements
        while (ptr1 < len(L1)) and (ptr2 < len(L2)):
            if L1[ptr1] < L2[ptr2]: # reverse
                res.append(L2[ptr2])
                ptr2 +=1
            else:
                res.append(L1[ptr1])
                ptr1 +=1
        
        # for the rest of the elements:
        while (ptr1 < len(L1)):
            res.append(L1[ptr1])
            ptr1 +=1
        while (ptr2 < len(L2)):
            res.append(L2[ptr2])
            ptr2 +=1

        return res # return combined list

    def mergeRecursive(L):
        """ Recursively break down the list into each sublist"""
        if len(L) < 2:
            return L
        
        half = len(L)//2
        left = mergeRecursive(L[:half])
        right = mergeRecursive(L[half:])

        return merge(left,right)
    
    return mergeRecursive(L)

# leetcode implementation:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Append any remaining elements
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        return mergeSort(nums)