from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemes, crud
from utils.db import get_db
from utils.auth import role_required
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/memberships", response_model=list[schemes.MemberShip])
async def read_memberships(db: Session = Depends(get_db), 
                       current_user: schemes.TokenData = Depends(role_required(["admin", "user"]))):
    return crud.get_memberships(db=db)

@router.post("/memberships", response_model=schemes.MemberShip)
async def create_membership(membership: schemes.MemberShipCreate, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    try:
        membership = crud.create_membership(db=db, membership=membership)
        return membership
    except IntegrityError as e:
        error_msg = e.orig.args[1]
        raise HTTPException(status_code=409, detail=error_msg)

@router.get("/memberships/{id}", response_model=schemes.MemberShip)
async def get_membership_by_id(id: int, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    membership = crud.get_membership(db=db, membership_id=id)
    if membership:
        return membership
    else:
        raise HTTPException(status_code=404, detail=f"Membership with id {id} not found.")
    
@router.put("/memberships", response_model=schemes.MemberShip)
async def put_membership(membership_update: schemes.MemberShip, db: Session = Depends(get_db), current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    membership = crud.get_membership(db=db, membership_id=membership_update.id)
    if membership:
        return crud.update_membership(db=db, membership_id=membership_update.id, membership_update=membership_update)
    else:
        raise HTTPException(status_code=404, detail=f"Membership with id {membership_update.id} not found.")
    
@router.delete("/memberships/{id}", response_model=schemes.MemberShip)
async def delete_membership(id: int, db: Session = Depends(get_db), 
                            current_user: schemes.TokenData = Depends(role_required(["admin"]))):
    membership = crud.get_membership(db=db, membership_id=id)
    if membership:
        return crud.delete_membership(db=db, membership_id=id)
    else:
        raise HTTPException(status_code=404, detail=f"Membership with id {id} not found.")