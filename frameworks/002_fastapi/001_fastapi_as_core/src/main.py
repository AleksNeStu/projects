from typing import List

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate, Page

from data.entities import users_data, trades_data
from models.pydantic import User, Trade
from utils import get_by_id
from validation.error import raise_not_found_err, raise_already_exist_err

app = FastAPI(
    title="Trading App"
)
# add_pagination - a function that adds pagination feature to the app.
add_pagination(app)

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


# USERS

# https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter
# There are some cases where you need or want to return some data that is not exactly what the type declares.
# @app.get("/users/{user_id}", response_model=List[User])
@app.get("/users/{user_id}")
def get_user(user_id: int) -> User:
    user = get_by_id(users_data, user_id)
    if not user:
        raise_not_found_err()
    return user


@app.post("/users/{user_id}")
def add_user(new_user: User):
    if get_by_id(users_data, new_user.id):
        raise_already_exist_err()

    users_data.append(new_user)  # rep case not control id primary key logic increment
    return users_data


@app.put("/users/{user_id}")
def update_user(new_user: User):
    user = get_user(new_user.id)
    user.update(new_user.model_dump())
    # TODO: Update users_data collection
    return users_data



# Pagination via offset and limit
@app.get("/users")
def get_users() -> LimitOffsetPage[User]:
    """
    If you use ORM/DB framework that you need to use paginate function that is specific to your framework. Otherwise,
    you will need to load all data into memory and then paginate it which is not good for performance.

    You can find more information about intergrations in Avaiable Integrations section.

    For instance, if you use SQLAlchemy you can use paginate from fastapi_pagination.ext.sqlalchemy module.
    """
    # paginate - a function that paginates data and returns Page instance.
    return paginate(users_data)


# TRADES

# Page Number Pagination
# https://uriyyo-fastapi-pagination.netlify.app/tutorials/page-number-pagination/
# Page - a class that represents a paginated data.
# Return type/response model is Page. It means that this endpoints can use paginate function
@app.get("/trades")
def get_trades() -> Page[Trade]:
    return paginate(trades_data)


# Response schema will contain:
#
# items - list of items paginated items.
# page - current page number.
# size - number of items per page.
# pages - total number of pages.
# total - total number of items

@app.post("/trades")
def add_trades(trades: List[Trade]):
    trades.extend(trades)
    return trades_data


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True, log_level="debug")
