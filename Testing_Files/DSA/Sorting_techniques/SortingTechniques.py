from typing import List
# Bubble Sort:

def bubbleSort1(arr: List[int]) -> None:
    """Sorts arr in place using bubble sort."""

    for idx1 in range(len(arr)):
        isSwapped = False
        for idx2 in range(len(arr)-idx1-1):
            if arr[idx2] > arr[idx2+1]:
                arr[idx2] , arr[idx2+1] = arr[idx2+1] , arr[idx2]
                isSwapped = True
        if not isSwapped: # if no swap occurs, stop, the list is sorted
            break

def bubbleSort2(arr: List[int]) -> None:
    """Sorts arr in place using bubble sort."""
    for idx1 in range(len(arr)):
        isSwapped = False
        for idx2 in range(1,len(arr)-idx1):
            if arr[idx2-1] > arr[idx2]:
                arr[idx2-1] , arr[idx2] = arr[idx2] , arr[idx2-1]
                isSwapped = True
        if not isSwapped:
            break

def bubbleSort3(arr: List[int]) -> None:
    swap = True
    while swap:
        swap = False
        for idx in range(len(arr)-1):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                swap = True



def selectionSortMAYBE(arr: List[int]) -> None:
    for idx1 in range(len(arr)):
        for idx2 in range(idx1+1,len(arr)):
            if arr[idx2] > arr[idx1]:
                arr[idx2] , arr[idx1] = arr[idx1], arr[idx2]


# Insertion Sort:
def insertionSort1(arr:List[int]) -> None:
    """ Sorts arr using insertion Sort."""
    for idx1 in range(1,len(arr)):

        key = arr[idx1]
        idx2 = idx1-1

        while((idx2 >=0 ) and (arr[idx2]> key)):
            arr[idx2+1] = arr[idx2]
            idx2 -=1

        arr[idx2+1] = key


# Selection Sort:

def selectionSort(arr: List[int]):
    suffixStart = 0
    while suffixStart != len(arr):
        for idx in range(suffixStart,len(arr)):
            if arr[suffixStart] > arr[idx]:
                arr[suffixStart], arr[idx] = arr[idx] , arr[suffixStart]
        suffixStart +=1

def selectionSort2(arr: List[int]):
    for suffixStart in range(0,len(arr)):
        minIndex = suffixStart
        for idx in range(suffixStart +1, len(arr)):
            if arr[minIndex] > arr[idx]:
                minIndex = idx
        arr[suffixStart], arr[minIndex] = arr[minIndex], arr[suffixStart]



# Merge Sort:

def mergeSort1(arr: List[int])-> List[int]:
    """ Returns a list sorted through merge sort."""
    def mergeSortMerger(L1,L2):
        ptr1 = ptr2 = 0
        res = []
        while ((ptr1 < len(L1)) and (ptr2 < len(L2))):
            if L1[ptr1] > L2[ptr2]:
                res.append(L2[ptr2])
                ptr2 +=1
            else:
                res.append(L1[ptr1])
                ptr1 +=1 
        
        while (len(L1)>ptr1):
            res.append(L1[ptr1])
            ptr1 +=1
        while (len(L2) > ptr2):
            res.append(L2[ptr2])
            ptr2 +=1
        return res
    
    def mergeSortRecur(L):
        if len(L) < 2:
            return L
        
        half = len(L)//2
        left = mergeSortRecur(L[:half])
        right = mergeSortRecur(L[half:])
        return mergeSortMerger(left,right)
    return mergeSortRecur(arr)


# quick sort:
def quickSort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr[:]
    
    pivot = len(arr)*3//4
    smaller = []
    equal = []
    larger = []

    for ele in arr:
        if ele < arr[pivot]:
            smaller.append(ele)
        elif ele > arr[pivot]:
            larger.append(ele)
        else: # == case
            equal.append(ele)

    return quickSort(smaller) + equal + quickSort(larger)
    
    



