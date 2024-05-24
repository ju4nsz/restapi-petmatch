from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemes, crud
from utils.db import get_db
from utils.auth import role_required
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/petstype", response_model=list[schemes.PetType])
async def read_petstype(db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    return crud.get_pets_type(db=db)

@router.post("/petstype", response_model=schemes.PetType)
async def create_pet_type(pet_type: schemes.PetTypeCreate, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    try:
        pet_type_db = crud.create_pet_type(db=db, pet_type=pet_type)
        return pet_type_db
    except IntegrityError as e:
        error_msg = e.orig.args[1]
        raise HTTPException(status_code=409, detail=error_msg)

@router.get("/petstype/{id}", response_model=schemes.PetType)
async def get_pet_type_by_id(id: int, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["user", "admin"]))):
    pet_type = crud.get_pet_type(db=db, pet_type_id=id)
    if pet_type:
        return pet_type
    else:
        raise HTTPException(status_code=404, detail=f"Pet type with id {id} not found.")
    
@router.put("/petstype", response_model=schemes.PetType)
async def put_pet_type(pet_type_update: schemes.PetType, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    pet_type = crud.get_pet_type(db=db, pet_type_id=pet_type_update.id)
    if pet_type:
        return crud.update_pet_type(db=db, pet_type_id=pet_type.id, pet_type_update=pet_type_update)
    else:
        raise HTTPException(status_code=404, detail=f"Pet Type with id {pet_type_update.id} not found.")
    
@router.delete("/petstype/{id}", response_model=schemes.MemberShip)
async def delete_pet_type(id: int, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    pet_type = crud.get_pet_type(db=db, pet_type_id=id)
    if pet_type:
        return crud.delete_pet_type(db=db, pet_type_id=id)
    else:
        raise HTTPException(status_code=404, detail=f"Pet type with id {id} not found.")