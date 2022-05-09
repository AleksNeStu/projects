"""pickle."""

import pickle
# for the file in which we are storing the object

shoplistfile = './shoplist.data'
# shopping list
shoplist = ['apples', 'mango', 'carrots']
# Writing to file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # putting object to the file
f.close()
del shoplist # destroying the variable shoplist
# reading from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # loading object from the file
print(storedlist)
