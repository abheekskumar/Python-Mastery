"""
import statistics as stats

L1 = list(range(1,101))
for x in L1:
    print(x)
print(stats.mean(L1))
print(stats.mode(L1))
print(stats.median(L1))

This is the traditional way of inporting modules
"""

from statistics import * # this imports all functions and attributes from that module into this namespace.

mode()
median()
mean()
L1 = list(range(1,101))
print(median(L1))