# Python code to demonstrate the working of
# random() and seed()

# importing "random" for random operations
import random

# using random() to generate a random number
# between 0 and 1
print ("A random number between 0 and 1 is : ", end="")
print (random.random())

# using seed() to seed a random number
random.seed(5)

# printing mapped random number
print ("The mapped random number with 5 is : ", end="")
print (random.random())

# using seed() to seed different random number
random.seed(7)

# printing mapped random number
print ("The mapped random number with 7 is : ", end="")
print (random.random())

# using seed() to seed to 5 again
random.seed(5)

# printing mapped random number
print ("The mapped random number with 5 is : ",end="")
print (random.random())

# using seed() to seed to 7 again
random.seed(7)

# printing mapped random number
print ("The mapped random number with 7 is : ",end="")
print (random.random())













# Python code to demonstrate the working of
# shuffle() and uniform()

# importing "random" for random operations
import random

# Initializing list
li = [1, 4, 5, 10, 2]

# Printing list before shuffling
print ("The list before shuffling is : ", end="")
for i in range(0, len(li)):
    print (li[i], end=" ")
print("\r")

# using shuffle() to shuffle the list
random.shuffle(li)

# Printing list after shuffling
print ("The list after shuffling is : ", end="")
for i in range(0, len(li)):
    print (li[i], end=" ")
print("\r")

# using uniform() to generate random floating number in range
# prints number between 5 and 10
print ("The random floating point number between 5 and 10 is : ",end="")
print (random.uniform(5,10))
