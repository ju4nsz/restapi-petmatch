from sqlalchemy.orm import Session
from utils.passwords import get_password_hash
from sqlalchemy.exc import IntegrityError
from . import models, schemes

def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()

def get_role_by_name(db: Session, name: str):
    return db.query(models.Role).filter(models.Role.name == name).first()

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()

def create_role(db: Session, role: schemes.RoleCreate):
    db_role = models.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def update_role(db: Session, role_id: int, role_update: schemes.RoleCreate):
    db_role = get_role(db, role_id)
    if db_role:
        for key, value in role_update.dict().items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemes.UserCreate):
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: schemes.UserUpdate):
    db_user = get_user(db, user_id)
    if db_user:
        user_update.password = get_password_hash(password=user_update.password)
        for key, value in user_update.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_membership(db: Session, membership_id: int):
    return db.query(models.MemberShip).filter(models.MemberShip.id == membership_id).first()

def get_membership_by_name(db: Session, name: str):
    return db.query(models.MemberShip).filter(models.MemberShip.name == name).first()

def get_memberships(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MemberShip).offset(skip).limit(limit).all()

def create_membership(db: Session, membership: schemes.MemberShipCreate):
    db_membership = models.MemberShip(**membership.dict())
    db.add(db_membership)
    db.commit()
    db.refresh(db_membership)
    return db_membership

def update_membership(db: Session, membership_id: int, membership_update: schemes.MemberShipCreate):
    db_membership = get_membership(db, membership_id)
    if db_membership:
        for key, value in membership_update.dict().items():
            setattr(db_membership, key, value)
        db.commit()
        db.refresh(db_membership)
    return db_membership

def delete_membership(db: Session, membership_id: int):
    db_membership = get_membership(db, membership_id)
    if db_membership:
        db.delete(db_membership)
        db.commit()
    return db_membership

def get_pet_type(db: Session, pet_type_id: int):
    return db.query(models.PetType).filter(models.PetType.id == pet_type_id).first()

def get_pets_type(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PetType).offset(skip).limit(limit).all()

def update_pet_type(db: Session, pet_type_id: int, pet_type_update: schemes.PetType):
    db_pet_type = get_pet_type(db, pet_type_id)
    if db_pet_type:
        for key, value in pet_type_update.dict().items():
            setattr(db_pet_type, key, value)
        db.commit()
        db.refresh(db_pet_type)
    return db_pet_type

def create_pet_type(db: Session, pet_type: schemes.PetTypeCreate):
    db_pet_type = models.PetType(**pet_type.dict())
    db.add(db_pet_type)
    db.commit()
    db.refresh(db_pet_type)
    return db_pet_type

def delete_pet_type(db: Session, pet_type_id: int):
    db_pet_type = get_pet_type(db, pet_type_id)
    if db_pet_type:
        db.delete(db_pet_type)
        db.commit()
    return db_pet_type

def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pet).offset(skip).limit(limit).all()

def update_pet(db: Session, pet_id: int, pet_update: schemes.PetUpdate):
    db_pet = get_pet(db, pet_id)
    if db_pet:
        for key, value in pet_update.dict().items():
            setattr(db_pet, key, value)
        db.commit()
        db.refresh(db_pet)
    return db_pet

def create_pet(db: Session, pet: schemes.PetCreate):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def delete_pet(db: Session, pet_id: int):
    db_pet = get_pet(db, pet_id)
    if db_pet:
        db.delete(db_pet)
        db.commit()
    return db_pet

def get_match(db: Session, pet_id: int):
    return db.query(models.Match).filter(
        (models.Match.first_pet_id == pet_id) | (models.Match.second_pet_id == pet_id)
    ).all()

def get_matches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Match).offset(skip).limit(limit).all()

def create_match(db: Session, match: schemes.MatchCreate):
    db_match = models.Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def delete_match(db: Session, match_id: int):
    db_match = get_match(db, match_id)
    if db_match:
        db.delete(db_match)
        db.commit()
    return db_match