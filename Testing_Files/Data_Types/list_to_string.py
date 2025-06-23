s1 = "Hello World! This is a string."
l1 = list(s1) # converting a string to a list of CHARACTERS
l2 = s1.split() # converting a string to a list of WORDS

s2 = "".join(l1) # converting a list of CHARACTERS to a string using an empty string
s3 = " ".join(l2) # converting a list of WORDS to a string using a whitespace

print(s1,l1,l2,s2,s3,sep = "\n")