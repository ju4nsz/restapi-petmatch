from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import crud
from utils import auth, db, passwords
from dotenv import load_dotenv
from datetime import timedelta
import os

router = APIRouter()

load_dotenv()

@router.post("/authenticate")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(db.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = crud.get_user_by_username(db=db, username=form_data.username)
    if user:
        if passwords.verify_password(plain_password=form_data.password, hashed_password=user.password):
            if user.is_active == 1:
                expires_minutes = int(os.getenv("TIMES_EXPIRES_TOKEN"))
                expires_delta = timedelta(minutes=expires_minutes)
                role = crud.get_role(db=db, role_id=user.role_id)
                access_token_jwt = auth.create_access_token(data={
                    "sub": user.username,
                    "role": role.name
                }, expires_delta=expires_delta)
                return {
                    "access_token": access_token_jwt,
                    "token_type": "Bearer"
                }
            else:
                raise credentials_exception
        else:
            raise credentials_exception
    else:
        raise credentials_exception