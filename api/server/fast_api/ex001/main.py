from fastapi import FastAPI, HTTPException
from mongita import MongitaClientDisk
from pydantic import BaseModel
import uvicorn

class Shape(BaseModel):
    name: str
    no_of_sides: int
    id: int

app = FastAPI()

client = MongitaClientDisk()
db = client.db 
shapes = db.shapes

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/shapes")
async def get_shapes():
    existing_shapes = shapes.find({})
    return [
        {key:shape[key] for key in shape if key != "_id"}
        for shape in existing_shapes
    ]

@app.get("/shapes/{shape_id}")
async def get_shape_by_id(shape_id: int):
    if shapes.count_documents({"id": shape_id}) > 0:
        shape = shapes.find_one({"id": shape_id})
        return {key:shape[key] for key in shape if key != "_id"}
    raise HTTPException(status_code=404, detail=f"No shape with id {shape_id} found")

@app.post("/shapes")
async def post_shape(shape: Shape):
    shapes.insert_one(shape.dict())
    return shape

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
  uvicorn.run("main:app", host="0.0.0.0", port=5000)