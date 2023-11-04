from typing import List

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination, paginate, Page

from data.entities import trades_data
from models.pydantic import Trade
from routers import users

app = FastAPI(
    title="Trading App"
)
# add_pagination - a function that adds pagination feature to the app.
add_pagination(app)
# routers
app.include_router(users.router)




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
