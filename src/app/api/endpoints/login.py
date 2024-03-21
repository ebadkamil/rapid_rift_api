from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

from src.app.api.deps import CurrentUser, SessionDep
from src.app.crud.users import authenticate_user
from src.app.models import Token
from src.app.utils import create_access_token

router = APIRouter()


@router.post("/token")
async def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return Token(access_token=create_access_token(user.id))


@router.get("/users/me")
async def read_users_me(current_user: CurrentUser):
    return current_user
