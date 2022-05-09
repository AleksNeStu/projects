#1) Indexing lists and tuples
list_values = [1, 2, 3]
set_values = (10, 20, 30)
print(list_values[0])
print(set_values[0])




#2) Changing values: lists vs tuples
list_values = [1, 2, 3]
set_values = (10, 20, 30)
list_values[0] = 100
print(list_values)
set_values[0] = 100




#3) Tuple vs List Expanding
list_values = [1, 2, 3]
set_values = (1, 2, 3)
print(id(list_values))
print(id(set_values))
print()

list_values += [4, 5, 6]
set_values += (4, 5, 6)
print(id(list_values))
print(id(set_values))




#4) Other Immutable Data Type Examples
number = 42
print(id(number))
number += 1
print(id(number))




text = "Data Science"
print(id(text))
text += " with Python"
print(id(text))



#5) Copying Mutable Objects by Reference
values = [4, 5, 6]
values2 = values
print(id(values))
print(id(values2))

values.append(7)
print(values is values2)
print(values)
print(values2)

#6) Copying Immutable Objects
text = "Python"
text2 = text
print(id(text))
print(id(text2))
print(text is text2)
print()

text += " is awesome"
print(id(text))
print(id(text2))
print(text is text2)
print()

print(text)
print(text2)