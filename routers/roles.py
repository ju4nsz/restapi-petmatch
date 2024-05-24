from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemes, crud
from utils.db import get_db
from utils.auth import role_required
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/roles", response_model=list[schemes.Role])
async def read_roles(db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin"]))):
    return crud.get_roles(db=db)

@router.post("/roles", response_model=schemes.Role)
async def create_role(role: schemes.RoleCreate, db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin"]))):
    try:
        role = crud.create_role(db=db, role=role)
        return role
    except IntegrityError as e:
        error_msg = e.orig.args[1]
        raise HTTPException(status_code=409, detail=error_msg)

@router.get("/roles/{id}", response_model=schemes.Role)
async def get_role_by_id(id: int, db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required([ "admin"]))):
    role = crud.get_role(db=db, role_id=id)
    if role:
        return role
    else:
        raise HTTPException(status_code=404, detail=f"Role with id {id} not found.")
    
@router.put("/roles", response_model=schemes.Role)
async def put_role(role_update: schemes.Role, db: Session = Depends(get_db),
                     current_user: schemes.TokenData = Depends(role_required([ "admin"]))):
    role = crud.get_role(db=db, role_id=role_update.id)
    if role:
        return crud.update_role(db=db, role_id=role_update.id, role_update=role_update)
    else:
        raise HTTPException(status_code=404, detail=f"Role with id {role_update.id} not found.")
    
@router.delete("/roles/{id}", response_model=schemes.Role)
async def delete_role(role_id: int, db: Session = Depends(get_db),
                     current_user: schemes.TokenData = Depends(role_required([ "admin"]))):
    role = crud.get_role(db=db, role_id=role_id)
    if role:
        return crud.delete_role(db=db, role_id=role_id)
    else:
        raise HTTPException(status_code=404, detail=f"Role with id {role_id} not found.")