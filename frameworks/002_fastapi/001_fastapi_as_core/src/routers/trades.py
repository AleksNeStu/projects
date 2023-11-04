from fastapi import APIRouter
from fastapi_pagination import paginate, Page

from data.entities import trades_data
from models.pydantic import Trade
from utils import crud

router = APIRouter(
    prefix="/trades",
    tags=["trades"],
    # dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)


# TRADES
# Page Number Pagination
# https://uriyyo-fastapi-pagination.netlify.app/tutorials/page-number-pagination/
# Page - a class that represents a paginated data.
# Return type/response model is Page. It means that this endpoints can use paginate function
@router.get("/")
def get_trades() -> Page[Trade]:
    return paginate(trades_data)


# Response schema will contain:
#
# items - list of items paginated items.
# page - current page number.
# size - number of items per page.
# pages - total number of pages.
# total - total number of items

@router.post("/")
def post_trades(nwe_trade: Trade):
    crud.create_record(trades_data, nwe_trade.model_dump())
    # trades.extend(trades)
    return trades_data
