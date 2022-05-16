from fastapi import APIRouter, Depends
from pydantic import BaseModel
from UserPostgresService import UserPostgresService
from di_container import Container
from dependency_injector.wiring import inject, Provide
#import jwt

router = APIRouter(
    prefix="/authorization"
)


class UserModel(BaseModel):
    email: str
    login: str
    password: str



@router.post("/registration")
@inject
async def create_user(
    db: UserModel,
    user_client: UserPostgresService = Depends(Provide[Container.user_client])
):
    await user_client.create_user(db.email, db.login, db.password)

