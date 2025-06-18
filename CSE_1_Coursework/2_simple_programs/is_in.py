
def isin(char,aStr):
    high = len(aStr)
    middle = (high)//2# concervative index for even cases
    # base case: when char is the middle(positive end) or 
    if len(aStr) == 0: # negative base case
        return False

    if len(aStr) == 1: # positive base case
        return aStr == char

    if char == aStr[middle]:
        return True
    # recursive case: when it's not in the middle, check above or below, based on that, recall the function
    else:
        if char > aStr[middle]:
            return isin(char,aStr[middle+1:]) # middle is included, so we use middle+1 due to includion of slicing
        else: # force char > aStr[middle]
            return isin(char,aStr[:middle]) # middle is already not included in search space due to exclusion of slicing

if __name__ == "__main__":
    char = "a"
    aStr = "bbcdkkknortuuvw"

    print(isin('f', 'bdefhllmsuvvvxyyyyz'))