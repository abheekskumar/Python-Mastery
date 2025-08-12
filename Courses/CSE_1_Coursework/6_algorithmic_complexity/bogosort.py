"""
Bogosort, monkey sort, stupid sort, slowsort, permutation sort, shotgun sort

Literally the stupidest thing I've heard.
It's random
"""
import random

def bogoSort(L):
    while not sorted(L):
        random.shuffle(L)
"""
best case: O(n)
worst case: unbounded, you could be here for a long time
worst best case: maybe n!, research and think about this.
"""
