from fastapi import APIRouter, HTTPException

from src.app.api.deps import InsepectDep, SecurityDep, SessionDep
from src.app.models import UserCreate


router = APIRouter()


@router.post("/open")
def create_open_user(user: UserCreate, session: SessionDep):
    user = crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_create = UserCreate.from_orm(user_in)
    user = crud.create_user(session=session, user_create=user_create)
    return user
