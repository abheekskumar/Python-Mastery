def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False


def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
    
""" non empty list and the fact that it should be in the list( or less than the first element)
The possibility of the element being beyond the list is missing.
"""