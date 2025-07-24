"""# file handling in python

# opening files:
#1:
# filehandle = open("pathto file w/ dir","AccessMODE")
# file handle = open(r"c:/dev/testing/text.txt","r") # raw string usage

#2: 
# with open("path","accessmode") as filehandle:
#       do some actions...
# auto closes once all the commands in the indentation are done

# close the file traditionally:
# filehandle.close()


# ways we usually work with files:
# try-except-else clause:
# 1) try:
# openthe file, do the actions
# 2) except:
# handle the exception
# else: close the file
# finally: nothing, pass # if the file doesn't open, this will produce an error


#Access mode:

r-reading pointer at the first, must exist
w-writing, pointer at the first, created
a- appending, pointer at the end, created
adding + at the ending adds the other functionality too 
adding "b" at the end or the beginning makes it a binary file

# manipulating the pointer:
try: # to handle opening the file
    fh = open("test.txt.",'w')
except IOError: # unable to open file
    print("Unable to open the file")
else: # to handle working with the file
    try:
        print(fh.tell()) # return position of the file pointer
        fh.seek(2) # displaces the position of the filepointer
        print(fh.tell())
    except Exception as e:
        print(f"{e} has been thrown")
    finally:
        fh.close()

# reading text file:
fh.read(n) - reads n bytes, by default, it's the entire file
fh.readline(n) - reads a line by default, if n specified, reads n bytes
fh.readlines() - returns all the strings as a list

note- both readline hand readlines will contain "\n" at the end
so to deal with that use line.rstrip("\n")
or while printing, change end argument to ""

Note- plain iteration through the filehandle is also just readlines
for line in fh == for line in fh.readlines()



# writing to text files:
fh.write(str1)  # writes string str1
fh.writelines(L[str]) # writes all the stirngs in L

# changes are held in buffer, if you're writing and then reading without closing the file,
# it's better to flush. Also prevents data loss
fh.flush()
# reading and writing to binaryfiles:
import pickle

x = pickle.load(fh) # reading
pickle.dump(obj,fh) # writing


# reading and writing csv files:
import csv

#reading:
csv_reader = csv.reader(fh,delimiter = ",") # create a reader object
for row in csv_reader: # iterating through each row
    print(row) 
# this leads to an EOF error( end of file error). and other newlines being inserted as
# the readerobject also converts the EOL character(\n) to a row
# to fix this, specify the opening clause as:
csv_reader = csv.reader(fh,delimiter= ",",newline="\n")
# writing
csv_writer = csv.writer(fh,delimiter=",") # creating a writer object
csv_writer.writerow() # just one row, could be an iterable
csv_writer.writerows() # an iterable containing each row


"""