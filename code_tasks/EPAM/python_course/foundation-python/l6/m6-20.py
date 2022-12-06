"""read()"""

#Open a file
fo = open("./test_file", "r+")
str = fo.read(10)
print ("Read String is : ", str)
# Close opend file
fo.close()


f = open("./test_file2", 'r', encoding = 'utf-8')
f1 = f.read(4)    # read the first 4 data
f2 = f.read(4)    # read the next 4 data
f3 = f.read()     # read in the rest till end of file
f4 = f.read()  # further reading returns empty sting

print("f1\n", f1)
print("f2\n", f2)
print("f3\n", f3)
print("f4\n", f4)




# read a file line-by-line using a for loop
for line in f:
    print(line, end='')

# read individual lines of a file
f5 = f.readline()
f6 = f.readline()
f7 = f.readline()
print("f5\n", f5)
print("f6\n", f6)
print("f7\n", f7)

# list of remaining lines of the entire file.
f8 = f.readlines()
print("f8\n", f8)