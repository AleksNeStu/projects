from data.entities import users_data
from fastapi import APIRouter
from fastapi_pagination import LimitOffsetPage, paginate

from models.pydantic import User
from utils import crud

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)


# https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter
# There are some cases where you need or want to return some data that is not exactly what the type declares.
# @app.get("/users/{user_id}", response_model=List[User])
@router.get("/{user_id}")
def get_user(user_id: int) -> User:
    user = crud.read_record(users_data, user_id)
    # user = get_by_id(users_data, user_id)
    # if not user:
    #     raise_not_found_err()
    return user


@router.post("/")
def post_user(new_user: User):
    crud.create_record(users_data, new_user.model_dump())
    # if get_by_id(users_data, new_user.id):
    #     raise_already_exist_err()
    #
    # users_data.append(new_user)  # rep case not control id primary key logic increment
    return users_data


@router.put("/")
def put_user(new_user: User):
    # user = get_user(new_user.id)
    # user.update(new_user.model_dump())
    # # TODO: Update users_data collection
    crud.update_record(users_data, new_user.model_dump())
    return users_data


@router.delete("/{user_id}")
def delete_user(user_id: int):
    crud.delete_record(users_data, user_id)
    return users_data


# Pagination via offset and limit
@router.get("/")
def get_users() -> LimitOffsetPage[User]:
    """
    If you use ORM/DB framework that you need to use paginate function that is specific to your framework. Otherwise,
    you will need to load all data into memory and then paginate it which is not good for performance.

    You can find more information about intergrations in Avaiable Integrations section.

    For instance, if you use SQLAlchemy you can use paginate from fastapi_pagination.ext.sqlalchemy module.
    """
    # paginate - a function that paginates data and returns Page instance.
    return paginate(users_data)
