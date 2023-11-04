class RecordNotFoundError(Exception):
    pass


class RecordAlreadyExistsError(Exception):
    pass


# Create (Add) a new record with a specific ID
def create_record(data, new_record):
    if any(record["id"] == new_record["id"] for record in data):
        raise RecordAlreadyExistsError("ID already exists")
    data.append(new_record)


# Read (Retrieve) a record by ID
def read_record(data, record_id):
    for record in data:
        if record["id"] == record_id:
            return record
    raise RecordNotFoundError("Record not found")


# Update (Modify) a record by ID
def update_record(data, record_id, new_data):
    for record in data:
        if record["id"] == record_id:
            record.update(new_data)
            return
    raise RecordNotFoundError("Record not found")


# Delete (Remove) a record by ID
def delete_record(data, record_id):
    for record in data:
        if record["id"] == record_id:
            data.remove(record)
            return
    raise RecordNotFoundError("Record not found")
