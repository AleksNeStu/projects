"""write()"""

file_relative_path = "./test_file"
fo = open(file=file_relative_path, mode='r+', encoding='utf-8')
fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()


# create a new file if it does not exist (if does, then overwrite)
with open("./test_file2",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")