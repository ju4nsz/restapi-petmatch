from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemes, crud
from utils.db import get_db
from utils.auth import role_required
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/pets", response_model=list[schemes.Pet])
async def read_pets(db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    return crud.get_pets(db=db)

@router.post("/pets", response_model=schemes.Pet)
async def create_pet(pet_base: schemes.PetBase, db: Session = Depends(get_db), 
                     current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    try:
        user = crud.get_user_by_username(db=db, username=current_user.username)
        pet_create = schemes.PetCreate(**pet_base.dict(), user_id=user.id)
        pet = crud.create_pet(db=db, pet=pet_create)
        return pet
    except IntegrityError as e:
        error_msg = e.orig.args[1]
        raise HTTPException(status_code=409, detail=error_msg)

@router.get("/pets/{id}", response_model=schemes.Pet)
async def get_pet_by_id(id: int, db: Session = Depends(get_db), 
                        current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    pet = crud.get_pet(db=db, pet_id=id)
    if pet:
        return pet
    else:
        raise HTTPException(status_code=404, detail=f"Pet with id {id} not found.")
    
@router.put("/pets", response_model=schemes.Pet)
async def put_pet(pet_update: schemes.PetUpdate, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    pet = crud.get_pet(db=db, pet_id=pet_update.id)
    if pet:
        return crud.update_pet(db=db, pet_id=pet.id, pet_update=pet_update)
    else:
        raise HTTPException(status_code=404, detail=f"Pet with id {pet_update.id} not found.")
    
@router.delete("/pets/{id}", response_model=schemes.Pet)
async def delete_pet(id: int, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    pet = crud.get_pet(db=db, pet_id=id)
    if pet:
        pet_type = crud.get_pet_type(db=db, pet_type_id=pet.pet_type_id)
        if pet_type:
            try:
                db_pet = crud.delete_pet(db=db, pet_id=id)
                return db_pet
            except IntegrityError as e:
                error_msg = e.orig.args[1]
                raise HTTPException(status_code=409, detail=error_msg)
        else:
            raise HTTPException(status_code=404, detail=f"Pet type with id {pet.pet_type_id} not found.")
    else:
        raise HTTPException(status_code=404, detail=f"Pet with id {id} not found.")