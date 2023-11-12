from fastapi import HTTPException


def raise_not_found_err():
    raise HTTPException(status_code=404, detail="Item not found")


def raise_already_exist_err():
    raise HTTPException(status_code=409, detail="Item already exist")
