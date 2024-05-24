from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemes, crud
from utils.db import get_db
from utils.auth import role_required
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/users", response_model=list[schemes.User])
async def read_users(db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin", "user"]))):
    return crud.get_users(db=db)

@router.post("/users", response_model=schemes.User)
async def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
    try:
        user = crud.create_user(db=db, user=user)
        return user
    except IntegrityError as e:
        error_msg = e.orig.args[1]
        raise HTTPException(status_code=409, detail=error_msg)

@router.get("/users/{id}", response_model=schemes.User)
async def get_user_by_id(id: int, db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin", "user"]))):
    user = crud.get_user(db=db, user_id=id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found.")
    
@router.put("/users", response_model=schemes.User)
async def put_user(user_update: schemes.UserUpdate, db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin", "user"]))):
    user = crud.get_user(db=db, user_id=user_update.id)
    if user:
        return crud.update_user(db=db, user_id=user_update.id, user_update=user_update)
    else:
        raise HTTPException(status_code=404, detail=f"User with id {user_update.id} not found.")
    
@router.delete("/users/{id}", response_model=schemes.User)
async def delete_user(id: int, db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin", "user"]))):
    user = crud.get_user(db=db, user_id=id)
    if user:
        return crud.delete_user(db=db, user_id=id)
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found.")