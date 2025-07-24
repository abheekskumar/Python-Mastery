def genSubsets(L):
    """ Returns all subsets of L"""

    if len(L) == 0: # base case
        return [[]] # return an empty list as a list
        
    most = genSubsets(L[:-1]) # all but the last element
    # 

    last = L[-1:] # for a particular iteration, obtain the last element
    new = [] # create a new list to store the subsets which also contain the last element
    for subset in most: # for each subset
        new.append(subset+last)# add the last element back and store it in new

    return most+new # return all the subsets without the last one(most) and with the last one(new)

    