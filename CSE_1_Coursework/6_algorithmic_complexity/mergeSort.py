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


def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [636,23,523,975,33,62,34,626,63]
print(mergeSort(L))
print(modSwapSort(L))
    
    
    




