# recur palin drome:

def recur_main_palindrome(s1):
    """
    a function that recursively checks whether a given string is an palindrome or not, recursively
    input: a string
    returns a boolean True or False
    """
    # Recursion implementation
    def recur_palindrome(l1):
        #print(l1)
        # base case: the len of string is either 0 or 1, it is a palindrome
        # recursive case: if len > 2, if the first and the last element, of the outermost elements are equal,check everything in between;
        # Base case:
        if (len(l1) == 0) or (len(l1) == 1):
            # it is a palindrome
            return True
        else: # recursive case, check the last two elements,if they are equal, check everything in between;
            if l1[0] == l1[-1]:
                # recur for the everything inbetween 
                return recur_palindrome(l1[1:-1])
            else:
                return False

    # string cleanup
    s2 = s1.lower()
    l1 = []
    valid_chars = "abcdefghijklmnopqrstuvwxyz"
    for i in s2:
        if i in valid_chars:
            l1.append(i)
    print(recur_palindrome(l1))
    

def iter_palindrome(s1):
    """
    a function that checks in given string is a palindrome or not, iteratively 
    input = string
    returs a boolean True or False
    """
    # string cleanup
    s2 = s1.lower()
    l1 = []
    valid_chars = "abcdefghijklmnopqrstuvwxyz"
    for i in s2:
        if i in valid_chars:
            l1.append(i)
    half_way = int(len(l1)/2)
    if len(l1)%2==0:
        # even number of characters
        num_loop = 0
        while True:
            for i in l1[:half_way:]:
                for j in l1[:half_way-1:-1]:
                    if i == j:
                        pass
                    else:
                        break
            num_loop +=1 
        
    else:
        # odd number of characters
        l1[:half_way:-1]
        l1[:half_way:]
        num_loop = 0
        while True:
            for i in l1[:half_way:]:
                for j in l1[:half_way:-1]:
                    if i == j:
                        pass
                    else:
                        break
            num_loop +=1 
if __name__ == "__main__":
    s1 = "racecar"
    recur_main_palindrome("ballab")
    recur_main_palindrome(s1)
    iter_palindrome(s1)