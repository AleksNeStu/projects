"""read()"""

f = open("./test_file2", 'r', encoding = 'utf-8')

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



