"""
Bubble sort: General idea is to compare adjacent elements and exchange them if the first one is
bigger than the second one.

algorithm:
for i in lower to upper:
    for j in lower to (upper -1 -i):
        if ar[j] > ar[j+1]:
            # swap them
            ar[j], ar[j+1] = ar[j+1], ar[j]

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