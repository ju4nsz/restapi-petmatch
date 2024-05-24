from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    description: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class MemberShipBase(BaseModel):
    name: str
    description: str

class MemberShipCreate(MemberShipBase):
    pass

class MemberShip(MemberShipBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullname: Optional[str] = None
    

class UserCreate(UserBase):
    password: str
    role_id: int
    membership_id: int

class UserUpdate(UserBase):
    id: int
    password: Optional[str] = None

class User(UserBase):
    id: int
    created_at: datetime
    role_id: int
    membership_id: int
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True

class PetTypeBase(BaseModel):
    name: str
    description: str

class PetTypeCreate(PetTypeBase):
    pass

class PetType(PetTypeBase):
    id: int

    class Config:
        orm_mode = True

class PetBase(BaseModel):
    name: str
    age: str
    pet_type_id: int

class PetCreate(PetBase):
    pet_type_id: int
    user_id: int

class PetUpdate(PetBase):
    id: int

class Pet(PetBase):
    id: int
    created_at: datetime
    user_id: int
    avaliability: int

    class Config:
        orm_mode = True

class MatchBase(BaseModel):
    first_pet_id: int
    second_pet_id: int

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    class Config:
        orm_mode = True
        
class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None