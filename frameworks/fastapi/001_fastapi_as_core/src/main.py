import json

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from routers import users, trades

app = FastAPI(
    title="Trading App"
)
# add_pagination - a function that adds pagination feature to the app.
add_pagination(app)
# routers
app.include_router(users.router)
app.include_router(trades.router)

# https://fastapi.tiangolo.com/tutorial/handling-errors/
@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    """Handle `Internal Server Error` in the of response stage."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.on_event("startup")
def save_openapi_json():
    openapi_data = app.openapi()
    # Change "openapi.json" to desired filename
    with open("openapi.json", "w") as file:
        json.dump(openapi_data, file)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True, log_level="debug")
