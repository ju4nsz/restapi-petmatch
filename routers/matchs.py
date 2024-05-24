from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemes, crud
from utils.db import get_db
from utils.auth import role_required
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/matchs", response_model=list[schemes.Match])
async def read_matches(db: Session = Depends(get_db), 
                       current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    return crud.get_matches(db=db)

@router.post("/matchs", response_model=schemes.Match)
async def create_match(match_create: schemes.MatchCreate, db: Session = Depends(get_db), 
                       current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    try:
        match = crud.create_match(db=db, match=match_create)
        return match
    except IntegrityError as e:
        error_msg = e.orig.args[1]
        raise HTTPException(status_code=409, detail=error_msg)

@router.get("/matchs/{id}", response_model=list[schemes.Match])
async def get_matchs_by_id_of_pet(id: int, db: Session = Depends(get_db), 
                       current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    pet = crud.get_pet(db=db, pet_id=id)
    if pet:
        matchs = crud.get_match(db=db, pet_id=id)
        return matchs
    else:
        raise HTTPException(status_code=404, detail=f"Pet with id {id} not found.")