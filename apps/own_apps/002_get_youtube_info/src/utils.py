import json


def find_key_values(data, target_key):
    found_values = []

    if isinstance(data, dict):
        if target_key in data:
            found_values.append(data[target_key])
        for key, value in data.items():
            found_values.extend(find_key_values(value, target_key))
    elif isinstance(data, list):
        for item in data:
            found_values.extend(find_key_values(item, target_key))
    return found_values


json_string = '''
{
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "state": [
            {"name": "A1"},
            {"name": "A2"}
        ],
        "country": "USA"
    },
    "friends": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 28}
    ]
}
'''

parsed_data = json.loads(json_string)
# The key you want to find
result = find_key_values(parsed_data, "name")
assert result == ['John', 'A1', 'A2', 'Alice', 'Bob']