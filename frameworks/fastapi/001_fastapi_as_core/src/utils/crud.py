from typing import List

from fastapi.exceptions import ResponseValidationError


# Create (Add) a new record with a specific ID
def create_record(data: List[dict], new_record: dict, raise_err: bool = True):
    new_id = new_record.get("id")
    if read_record(data, new_id, raise_err=False):
        raise ResponseValidationError(f"Record `{new_id}` already exists")
    data.append(new_record)
    return data



# Read (Retrieve) a record by ID
def read_record(data: List[dict], record_id: int, raise_err: bool = True):
    for record in data:
        if record.get("id") == record_id:
            return record

    if raise_err:
        raise ResponseValidationError(f"Record `{record_id}` not found")


# Update (Modify) a record by ID
def update_record(data: List[dict], new_data: dict, raise_err: bool = True):
    new_id = new_data.get("id")
    for record in data:
        if record.get("id") == new_id:
            record.update(new_data)
            return data

    if raise_err:
        raise ResponseValidationError(f"Record `{new_id}` not found")


# Delete (Remove) a record by ID
def delete_record(data: List[dict], record_id: int, raise_err: bool = True):
    for record in data:
        if record.get("id") == record_id:
            data.remove(record)  # using `remove` suppose to have unique records
            return data

    if raise_err:
        raise ResponseValidationError(f"Record `{record_id}` not found")
