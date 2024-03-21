from fastapi import APIRouter, HTTPException

from src.app.api.deps import SessionDep
from src.app.crud.users import create_user, get_user_by_email
from src.app.models import UserCreate

router = APIRouter()


@router.post("/open")
def create_open_user(user: UserCreate, session: SessionDep):
    user_exist = get_user_by_email(session=session, email=user.email)
    if user_exist:
        raise HTTPException(
            status_code=400,
            detail=f"The user with this email {user.email} already exists in the system",
        )
    user_create = UserCreate.from_orm(user)
    user = create_user(user_create=user_create, session=session)
    return user
