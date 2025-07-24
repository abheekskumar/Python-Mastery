s1 = "Hello World! This is a string."
l1 = list(s1) # converting a string to a list of CHARACTERS


# Split: called on a string, converts a string into a list based on argument given
l2 = s1.split() # converting a string to a list of WORDS
# l3 = s1.split("") # not allowed, use list(string) to obtain a list of characters.

# Join: called on a string instance, takes in a list as an attribute, converts 
# a list into a string
s2 = "".join(l1) # converting a list of CHARACTERS to a string using an empty string
s3 = " ".join(l2) # converting a list of WORDS to a string using a whitespace

print(s1,l1,l2,s2,s3,sep = "\n")