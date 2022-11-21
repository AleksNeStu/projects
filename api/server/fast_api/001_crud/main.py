import os

import uvicorn
from fastapi import FastAPI, HTTPException
from mongita import MongitaClientDisk
# GridFS is a convention drivers use to store and retrieve BSON binary data (type “\x05”) that exceeds MongoDB’s
# BSON-document size limit of 16 MiB.

from mongita import MongitaClientMemory
from pymongo import MongoClient
from pydantic import BaseModel

SHAPES = [
    {"name": "name_1", "no_of_sides": 21, "id": 1},
    {"name": "name_2", "no_of_sides": 22, "id": 2},
    {"name": "name_3", "no_of_sides": 23, "id": 3},
]

DB_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'db'))


class Shape(BaseModel):
    name: str
    no_of_sides: int
    id: int

app = FastAPI()

# client = MongitaClientDisk(host=DB_DIR)
# client = MongitaClientMemory()
client = MongoClient("localhost", 27017)
# client_db.test()



db = client.db
shapes = db.shapes
shapes.count_documents({})
dbs = client.list_database_names()


@app.get("/")
async def root():
    return {"message": "Hello world"}
"""
curl -X 'GET' \
  'http://127.0.0.1:5000/' \
  -H 'accept: application/json'
"""

def repr_snape(shape):
    return {key: shape[key] for key in shape if key != "_id"}


@app.get("/shapes")
async def get_shapes():
    existing_shapes = shapes.find({})
    return [repr_snape(shape) for shape in existing_shapes]


@app.get("/shapes/{shape_id}")
async def get_shape_by_id(shape_id: int):
    if shapes.count_documents({"id": shape_id}) > 0:
        shape = shapes.find_one({"id": shape_id})
        return repr_snape(shape)
    raise HTTPException(status_code=404, detail=f"No shape with id {shape_id} found")


@app.post("/shapes")
async def post_shape(shape: Shape):
    shapes.insert_one(shape.dict())
    return shape
"""
curl -X 'POST' \
  'http://127.0.0.1:5000/shapes' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test1",
  "no_of_sides": 2,
  "id": 1
}'
"""

"""
https://httpie.io/
http POST 127.0.0.1:5000/shapes name=new1 no_of_sides=99 id=4
"""


@app.put("/shapes/{shape_id}")
async def update_shape(shape_id: int, shape: Shape):
    if shapes.count_documents({"id": shape_id}) > 0:
        shapes.replace_one({"id": shape_id}, shape.dict())
        return shape
    raise HTTPException(status_code=404, detail=f"No shape with id {shape_id} found")


@app.put("/shapes/upsert/{shape_id}")
async def update_shape(shape_id: int, shape: Shape):
    shapes.replace_one({"id": shape_id}, shape.dict(), upsert=True)
    return shape


@app.delete("/shapes/{shape_id}")
async def delete_shape(shape_id: int):
    delete_result = shapes.delete_one({"id": shape_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"No shape with {shape_id} exists")
    return {"OK": True}


if __name__ == '__main__':
  # Insert init data
  for shape in SHAPES:
      if shapes.count_documents({"id": shape["id"]}) == 0:
          shapes.insert_one(shape)

  uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)