import json

#Convert from JSON to Python:

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(type(y), y)


# Convert from Python to JSON
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(type(y), y)