from sqlmodel import Session, select
from src.app.models import UserCreate, User
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(user_create: UserCreate, session: Session):
    hashed_password = get_password_hash(user_create.password)
    db_obj = User(**user_create.dict(), hashed_password=hashed_password)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

