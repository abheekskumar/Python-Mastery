def oddTuples(aTup):
    """
    Function that returns a tuple with every other element in aTup
    """
    tup2 = ()
    index = 0
    while index < len(aTup):
        tup2 += aTup[index],
        index +=2
     
    return tup2

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))

