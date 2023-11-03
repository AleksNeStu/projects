"""file object - attribute."""
# Open a file

file_relative_path = "./test_file"
fo = open(file=file_relative_path, mode='r+', encoding='utf-8')

print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)