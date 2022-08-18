from fastapi import APIRouter, Depends
from pydantic import BaseModel
from UserPostgresService import UserPostgresService
from di_container import Container
from dependency_injector.wiring import inject, Provide
from decouple import config
from api_film import popular, p, recommendations, recommendation
import jwt
import time

router = APIRouter(
    prefix="/authorization"
)


class UserModel(BaseModel):
    email: str
    login: str
    password: str

class Token(UserModel):
    token: str

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token: str):
    return {
        "access_token": token
    }


@router.get("/api_film")
async def api(id):
    return popular
    # return {"title":recommendation.title,
    #         "name":recommendation.overview}
    print("jopa")



@router.post("/registration")
@inject
async def create_user(
    db: UserModel,
    user_client: UserPostgresService = Depends(Provide[Container.user_client])
):
    try:
        payload = {
            "login": db.login,
            "expris": time.time() + 600
        }
        token = jwt.encode(payload,JWT_SECRET, algorithm=JWT_ALGORITHM)
        await user_client.create_user(db.email, db.login, db.password, token)
        return token_response(token)
    except:
        None


