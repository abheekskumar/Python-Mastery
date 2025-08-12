# Common operations:
seq = list()
seq1 = list(seq)
seq2 = list()
e = 0
# seq[1] # indexing
len(seq) # length
seq1 + seq2 # concatenation with the exception of range(it generates differently under the hood)
2*seq # replication with the exception of range " "
seq[0:3] # slicing [)- start is included, end is excluded
e in seq # membership operator, returns boolean
for e in seq: # iterates over a sequence
    pass


"""
Properties of data structures(so far):
str - characters, immutable
tuple - any, immutable
range - int, immutable, special due to the way they're generated
list - any, mutable

"""


r = range(1,101)
print(r[0:23]) # generates the range object with different boudaries, 
# doesn't produce an iterable.
# for ele in r:
    # print(ele)