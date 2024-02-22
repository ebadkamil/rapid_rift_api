from passlib.context import CryptContext
from sqlmodel import Session, select

from src.app.models import User, UserCreate

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


def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    return user


def authenticate_user(session: Session, email: str, password: str):
    user = get_user_by_email(session, email)
    if not user:
        return
    verify = verify_password(password, user.hashed_password)
    if not verify:
        return

    return user