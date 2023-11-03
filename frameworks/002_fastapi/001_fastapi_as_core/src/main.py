from typing import List

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from fastapi.responses import JSONResponse

from data.entities import users_data, trades_data
from models.pydantic import User, Trade
from utils import get_by_id

app = FastAPI(
    title="Trading App"
)


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


# https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter
# There are some cases where you need or want to return some data that is not exactly what the type declares.
# @app.get("/users/{user_id}", response_model=List[User])
@app.get("/users/{user_id}")
def get_user(user_id: int) -> User:
    user = get_by_id(users_data, user_id)
    return user


@app.get("/users")
def get_users() -> List[User]:
    return users_data


@app.get("/trades")
def get_trades() -> List[Trade]:
    return trades_data


@app.post("/trades")
def add_trades(trades: List[Trade]):
    trades.extend(trades)
    return trades_data


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True, log_level="debug")
