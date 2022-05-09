"""open()"""
file_relative_path = "./test_file"
file_full_path = "/Projects/sessions/s6/test_file"

# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):

#file
f1 = open(file_relative_path, mode='r', buffering=True) # open file in current directory
f2 = open(file_full_path)  # specifying full path


#mode
"""
Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or 
    truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists,
    the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a 
    new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
"""

f3 = open(file_relative_path)      # equivalent to 'r' or 'rt'
f4 = open(file_relative_path,'w')  # write in text mode
f5 = open(file_relative_path,'r+b') # read and write in binary mode

#encoding
f6 = open(file=file_relative_path, mode='r+', encoding='utf-8')


#
# lsof ./test_file


#close
f6.close()

# safer way 1
f7 = open(file=file_relative_path, mode='r+', encoding='utf-8')
try:
    f7.write("new_str")
finally:
    f7.close()

# safer way 2
with open(file=file_relative_path, mode='r+', encoding='utf-8') as f8:
  f8.write("new_str2")


print("done")

"""
Python File Methods
close()	Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and
          return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()	Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)	Read atmost n characters form the file. Reads till end of file if
          it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n
                  bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at
                  most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in
                              reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not
                      specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters
          written.
writelines(lines)   Write a list of lines to the file.
"""