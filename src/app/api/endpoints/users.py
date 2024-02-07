from fastapi import APIRouter, HTTPException

from src.app.api.deps import InsepectDep, SecurityDep, SessionDep
from src.app.models import UserCreate
from src.app.crud.users import create_user

router = APIRouter()


@router.post("/open")
def create_open_user(user: UserCreate, session: SessionDep):
    user_create = UserCreate.from_orm(user)
    user = create_user(session=session, user_create=user_create)
    return user
